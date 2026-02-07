"""
Management command to load Nigerian location data into the database
"""
from django.core.management.base import BaseCommand
from django.db import transaction
from django_ng_locations.models import Zone, State, LGA, City, Ward, PostalCode
from django_ng_locations.fixtures.nigeria_data import NIGERIA_DATA


class Command(BaseCommand):
    help = "Load Nigerian geographic data (zones, states, LGAs) into the database"

    def add_arguments(self, parser):
        parser.add_argument(
            "--clear",
            action="store_true",
            help="Clear existing data before loading",
        )

    def handle(self, *args, **options):
        if options["clear"]:
            self.stdout.write(self.style.WARNING("Clearing existing data..."))
            PostalCode.objects.all().delete()
            Ward.objects.all().delete()
            City.objects.all().delete()
            LGA.objects.all().delete()
            State.objects.all().delete()
            Zone.objects.all().delete()
            self.stdout.write(self.style.SUCCESS("Existing data cleared."))

        self.stdout.write("Loading Nigerian location data...")

        with transaction.atomic():
            zones_created = 0
            states_created = 0
            lgas_created = 0

            for zone_name, zone_data in NIGERIA_DATA.items():
                # Create or get zone
                zone, created = Zone.objects.get_or_create(
                    name=zone_name,
                    defaults={"code": zone_data["code"]}
                )
                if created:
                    zones_created += 1
                    self.stdout.write(f"  Created zone: {zone_name}")

                # Create states
                for state_name, state_data in zone_data["states"].items():
                    state, created = State.objects.get_or_create(
                        name=state_name,
                        defaults={
                            "zone": zone,
                            "code": state_data.get("code", ""),
                            "capital": state_data.get("capital", ""),
                        }
                    )
                    if created:
                        states_created += 1
                        self.stdout.write(f"    Created state: {state_name}")
                    elif state.zone != zone:
                        # Update zone if it changed
                        state.zone = zone
                        state.save()

                    # Create LGAs
                    for lga_name in state_data["lgas"]:
                        lga, created = LGA.objects.get_or_create(
                            state=state,
                            name=lga_name,
                            defaults={"code": ""}
                        )
                        if created:
                            lgas_created += 1

        self.stdout.write(
            self.style.SUCCESS(
                f"\nSuccessfully loaded Nigerian location data:\n"
                f"  - {zones_created} zones created\n"
                f"  - {states_created} states created\n"
                f"  - {lgas_created} LGAs created\n"
                f"\nTotal in database:\n"
                f"  - {Zone.objects.count()} zones\n"
                f"  - {State.objects.count()} states\n"
                f"  - {LGA.objects.count()} LGAs"
            )
        )

