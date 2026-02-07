# Testing Guide - Django NG Locations

This guide will help you test the package to ensure everything works correctly.

## Step 1: Initial Setup

### Create and Activate Virtual Environment (Recommended)

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python -m venv venv
source venv/bin/activate
```

### Install Django

```bash
pip install Django>=4.0
```

## Step 2: Run Migrations

```bash
# Create migrations for the package
python manage.py makemigrations django_ng_locations

# Apply migrations
python manage.py migrate
```

**Expected Output:**
```
Migrations for 'django_ng_locations':
  django_ng_locations\migrations\0001_initial.py
    - Create model Zone
    - Create model State
    - Create model LGA
    - Create model City
    - Create model Ward
    - Create model PostalCode
```

## Step 3: Load Data

```bash
python manage.py load_ng_locations
```

**Expected Output:**
```
Loading Nigerian location data...
  Created zone: North Central
  Created zone: North East
  ...
Successfully loaded Nigerian location data:
  - 6 zones created
  - 37 states created
  - 774 LGAs created
```

## Step 4: Verify Data in Django Shell

```bash
python manage.py shell
```

Run these commands in the shell:

```python
from django_ng_locations.models import Zone, State, LGA

# Test 1: Check zones
zones = Zone.objects.all()
print(f"✓ Total zones: {zones.count()} (Expected: 6)")
assert zones.count() == 6, "Should have 6 zones"

# Test 2: Check states
states = State.objects.all()
print(f"✓ Total states: {states.count()} (Expected: 37)")
assert states.count() == 37, "Should have 37 states (36 + FCT)"

# Test 3: Check LGAs
lgas = LGA.objects.all()
print(f"✓ Total LGAs: {lgas.count()} (Expected: 774)")
assert lgas.count() == 774, "Should have 774 LGAs"

# Test 4: Check zone relationships
for zone in zones:
    state_count = zone.states.count()
    print(f"✓ {zone.name}: {state_count} states")

# Test 5: Check specific state
lagos = State.objects.get(name="Lagos")
print(f"✓ Lagos state found")
print(f"  - Zone: {lagos.zone.name}")
print(f"  - Capital: {lagos.capital}")
print(f"  - Code: {lagos.code}")
print(f"  - LGAs: {lagos.lgas.count()}")
assert lagos.zone.name == "South West", "Lagos should be in South West"
assert lagos.lgas.count() == 20, "Lagos should have 20 LGAs"

# Test 6: Check LGA relationships
ikeja = LGA.objects.get(name="Ikeja", state=lagos)
print(f"✓ Ikeja LGA found in Lagos")

# Test 7: Test utility functions
from django_ng_locations.utils import (
    get_states_by_zone,
    get_lgas_by_state,
    get_state_by_name,
    search_locations
)

south_west = get_states_by_zone("South West")
print(f"✓ South West has {south_west.count()} states (Expected: 6)")
assert south_west.count() == 6, "South West should have 6 states"

lagos_lgas = get_lgas_by_state("Lagos")
print(f"✓ Lagos has {lagos_lgas.count()} LGAs")

state = get_state_by_name("Kano")
print(f"✓ Found state: {state.name}")

results = search_locations("Ikeja")
print(f"✓ Search for 'Ikeja' found:")
print(f"  - {results['lgas'].count()} LGAs")
print(f"  - {results['cities'].count()} cities")

print("\n✅ All tests passed!")
```

## Step 5: Test Django Admin

### Create Superuser

```bash
python manage.py createsuperuser
```

Follow the prompts to create a superuser account.

### Run Development Server

```bash
python manage.py runserver
```

### Access Admin Interface

1. Open browser: http://127.0.0.1:8000/admin
2. Login with superuser credentials
3. Verify you can see:
   - Geopolitical Zones
   - States
   - Local Government Areas
   - Cities
   - Wards
   - Postal Codes

### Test Admin Features

1. **View Zones**: Click on "Geopolitical Zones"
   - Should see 6 zones
   - Check state count column

2. **View States**: Click on "States"
   - Should see 37 states
   - Test search functionality
   - Test zone filter
   - Click on a state to view details

3. **View LGAs**: Click on "Local Government Areas"
   - Should see 774 LGAs
   - Test search functionality
   - Test state and zone filters
   - Verify autocomplete on state field

## Step 6: Test Package Building

### Install Build Tools

```bash
pip install build twine
```

### Build the Package

```bash
python -m build
```

**Expected Output:**
```
Successfully built django_ng_locations-0.1.0.tar.gz and django_ng_locations-0.1.0-py3-none-any.whl
```

### Check Distribution Files

```bash
# Windows
dir dist

# Linux/Mac
ls -l dist/
```

Should see:
- `django_ng_locations-0.1.0.tar.gz`
- `django_ng_locations-0.1.0-py3-none-any.whl`

### Test Local Installation

```bash
# Create a new virtual environment for testing
python -m venv test_env

# Activate it
# Windows: test_env\Scripts\activate
# Linux/Mac: source test_env/bin/activate

# Install from wheel
pip install dist/django_ng_locations-0.1.0-py3-none-any.whl

# Test import
python -c "from django_ng_locations.models import State; print('✓ Package installed successfully')"
```

## Step 7: Test Data Reload

```bash
# Clear and reload data
python manage.py load_ng_locations --clear
```

**Expected Output:**
```
Clearing existing data...
Existing data cleared.
Loading Nigerian location data...
...
Successfully loaded Nigerian location data
```

## Common Issues and Solutions

### Issue: Migration already exists

**Solution:**
```bash
# Delete existing migrations (except __init__.py)
# Then run:
python manage.py makemigrations django_ng_locations
python manage.py migrate
```

### Issue: Data already exists

**Solution:**
```bash
python manage.py load_ng_locations --clear
```

### Issue: Import errors

**Solution:**
```bash
# Make sure package is installed
pip install -e .

# Or reinstall
pip uninstall django-ng-locations
pip install -e .
```

### Issue: Admin not showing models

**Solution:**
Check that `django_ng_locations` is in `INSTALLED_APPS` in settings.py

## Checklist

- [ ] Migrations created successfully
- [ ] Migrations applied successfully
- [ ] Data loaded successfully (6 zones, 37 states, 774 LGAs)
- [ ] Django shell tests pass
- [ ] Utility functions work correctly
- [ ] Superuser created
- [ ] Admin interface accessible
- [ ] All models visible in admin
- [ ] Search and filters work in admin
- [ ] Package builds successfully
- [ ] Distribution files created
- [ ] Package installs from wheel
- [ ] Data reload works with --clear flag

## Performance Tests

```python
# In Django shell
import time
from django_ng_locations.models import State, LGA

# Test query performance
start = time.time()
states = list(State.objects.select_related('zone').all())
end = time.time()
print(f"✓ Loaded {len(states)} states in {end-start:.4f} seconds")

start = time.time()
lgas = list(LGA.objects.select_related('state', 'state__zone').all())
end = time.time()
print(f"✓ Loaded {len(lgas)} LGAs in {end-start:.4f} seconds")
```

## Next Steps After Testing

1. ✅ All tests pass → Ready to publish
2. ❌ Tests fail → Fix issues and retest
3. 📝 Document any issues found
4. 🚀 Proceed to publishing (see PUBLISHING.md)

## Support

If you encounter issues during testing:
1. Check this guide for solutions
2. Review error messages carefully
3. Check Django and Python versions
4. Create an issue on GitHub (after publishing)

