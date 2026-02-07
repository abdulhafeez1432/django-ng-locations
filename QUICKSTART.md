# Quick Start Guide - Django NG Locations

This guide will help you get started with the `django-ng-locations` package in just a few minutes.

## For This Development Project

Since you're working on the package itself, follow these steps:

### 1. Install Django (if not already installed)

```bash
pip install Django>=4.0
```

### 2. Run Migrations

```bash
python manage.py makemigrations django_ng_locations
python manage.py migrate
```

### 3. Load Nigerian Location Data

```bash
python manage.py load_ng_locations
```

### 4. Create a Superuser

```bash
python manage.py createsuperuser
```

### 5. Run the Development Server

```bash
python manage.py runserver
```

### 6. Access the Admin Interface

Open your browser and go to: http://127.0.0.1:8000/admin

Login with your superuser credentials and explore:
- Geopolitical Zones
- States
- Local Government Areas (LGAs)
- Cities
- Wards
- Postal Codes

## For Users Installing the Package

### 1. Install the Package

```bash
pip install django-ng-locations
```

### 2. Add to INSTALLED_APPS

Edit your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_ng_locations',
    ...
]
```

### 3. Run Migrations

```bash
python manage.py migrate
```

### 4. Load Data

```bash
python manage.py load_ng_locations
```

### 5. Start Using It!

```python
from django_ng_locations.models import State, LGA
from django_ng_locations.utils import get_states_by_zone

# Get all states
states = State.objects.all()

# Get states in a specific zone
south_west = get_states_by_zone("South West")

# Get LGAs in Lagos
lagos_lgas = LGA.objects.filter(state__name="Lagos")
```

## Testing the Package

### Run Python Shell

```bash
python manage.py shell
```

### Try These Commands

```python
# Import models
from django_ng_locations.models import Zone, State, LGA

# Check zones
zones = Zone.objects.all()
print(f"Total zones: {zones.count()}")
for zone in zones:
    print(f"- {zone.name}: {zone.states.count()} states")

# Check states
states = State.objects.all()
print(f"\nTotal states: {states.count()}")

# Check LGAs
lgas = LGA.objects.all()
print(f"Total LGAs: {lgas.count()}")

# Get specific state
lagos = State.objects.get(name="Lagos")
print(f"\n{lagos.name}:")
print(f"  Zone: {lagos.zone.name}")
print(f"  Capital: {lagos.capital}")
print(f"  LGAs: {lagos.lgas.count()}")

# List Lagos LGAs
print("\nLagos LGAs:")
for lga in lagos.lgas.all()[:5]:
    print(f"  - {lga.name}")

# Use utility functions
from django_ng_locations.utils import get_lgas_by_state, search_locations

# Get all LGAs in a state
kano_lgas = get_lgas_by_state("Kano")
print(f"\nKano has {kano_lgas.count()} LGAs")

# Search for locations
results = search_locations("Ikeja")
print(f"\nSearch results for 'Ikeja':")
print(f"  States: {results['states'].count()}")
print(f"  LGAs: {results['lgas'].count()}")
```

## Building the Package for Distribution

### 1. Install Build Tools

```bash
pip install build twine
```

### 2. Build the Package

```bash
python -m build
```

This creates distribution files in the `dist/` directory.

### 3. Test Installation Locally

```bash
pip install dist/django_ng_locations-0.1.0-py3-none-any.whl
```

### 4. Upload to PyPI

```bash
python -m twine upload dist/*
```

See `PUBLISHING.md` for detailed publishing instructions.

## Common Tasks

### Reload Data

If you need to reload the data:

```bash
python manage.py load_ng_locations --clear
```

### Check Data Integrity

```python
from django_ng_locations.models import Zone, State, LGA

# Verify all states have zones
states_without_zones = State.objects.filter(zone__isnull=True)
print(f"States without zones: {states_without_zones.count()}")

# Verify all LGAs have states
lgas_without_states = LGA.objects.filter(state__isnull=True)
print(f"LGAs without states: {lgas_without_states.count()}")

# Count by zone
for zone in Zone.objects.all():
    print(f"{zone.name}: {zone.states.count()} states, "
          f"{LGA.objects.filter(state__zone=zone).count()} LGAs")
```

### Export Data

```bash
# Export as JSON fixture
python manage.py dumpdata django_ng_locations --indent 2 > ng_locations_backup.json

# Import back
python manage.py loaddata ng_locations_backup.json
```

## Next Steps

1. Read the full documentation in `README.md`
2. Check out usage examples in `EXAMPLE_USAGE.md`
3. Learn how to publish the package in `PUBLISHING.md`
4. Contribute improvements via `CONTRIBUTING.md`

## Troubleshooting

### Migration Issues

If you encounter migration issues:

```bash
python manage.py makemigrations
python manage.py migrate --run-syncdb
```

### Data Not Loading

Make sure you've run migrations before loading data:

```bash
python manage.py migrate
python manage.py load_ng_locations --clear
```

### Import Errors

Make sure the package is in your Python path:

```bash
pip install -e .  # For development
# or
pip install django-ng-locations  # For production
```

## Support

- GitHub Issues: https://github.com/yourusername/django-ng-locations/issues
- Documentation: See README.md
- Examples: See EXAMPLE_USAGE.md

