from django.contrib import admin
from .models import Zone, State, LGA, City, Ward, PostalCode


@admin.register(Zone)
class ZoneAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "state_count")
    search_fields = ("name", "code")
    ordering = ("name",)

    def state_count(self, obj):
        return obj.states.count()
    state_count.short_description = "Number of States"


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ("name", "zone", "code", "capital", "lga_count")
    list_filter = ("zone",)
    search_fields = ("name", "code", "capital")
    ordering = ("name",)
    autocomplete_fields = ["zone"]

    def lga_count(self, obj):
        return obj.lgas.count()
    lga_count.short_description = "Number of LGAs"


@admin.register(LGA)
class LGAAdmin(admin.ModelAdmin):
    list_display = ("name", "state", "zone_name", "code", "city_count", "ward_count")
    list_filter = ("state__zone", "state")
    search_fields = ("name", "code", "state__name")
    ordering = ("state__name", "name")
    autocomplete_fields = ["state"]

    def zone_name(self, obj):
        return obj.state.zone.name
    zone_name.short_description = "Zone"

    def city_count(self, obj):
        return obj.cities.count()
    city_count.short_description = "Cities"

    def ward_count(self, obj):
        return obj.wards.count()
    ward_count.short_description = "Wards"


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ("name", "lga", "state_name", "is_capital", "population")
    list_filter = ("is_capital", "lga__state__zone", "lga__state")
    search_fields = ("name", "lga__name", "lga__state__name")
    ordering = ("name",)
    autocomplete_fields = ["lga"]

    def state_name(self, obj):
        return obj.lga.state.name
    state_name.short_description = "State"


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ("name", "lga", "state_name", "code")
    list_filter = ("lga__state__zone", "lga__state")
    search_fields = ("name", "code", "lga__name", "lga__state__name")
    ordering = ("lga__state__name", "lga__name", "name")
    autocomplete_fields = ["lga"]

    def state_name(self, obj):
        return obj.lga.state.name
    state_name.short_description = "State"


@admin.register(PostalCode)
class PostalCodeAdmin(admin.ModelAdmin):
    list_display = ("code", "area", "lga", "city", "state_name")
    list_filter = ("lga__state__zone", "lga__state")
    search_fields = ("code", "area", "lga__name", "city__name", "lga__state__name")
    ordering = ("code",)
    autocomplete_fields = ["lga", "city"]

    def state_name(self, obj):
        return obj.lga.state.name
    state_name.short_description = "State"

