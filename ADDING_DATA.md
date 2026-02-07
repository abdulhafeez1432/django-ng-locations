# Adding Your Own Data - Django NG Locations

The `django-ng-locations` package comes with complete data for **zones, states, and LGAs**. However, the models for **cities, wards, and postal codes** are ready for you to add your own data.

## What's Included vs What You Can Add

### ✅ Included (Loaded Automatically)
- 6 Geopolitical Zones
- 37 States (with codes and capitals)
- 774 Local Government Areas

### 📋 Models Ready (You Can Add Data)
- Cities
- Wards
- Postal Codes

## How to Add Data

### Option 1: Using Django Admin

The easiest way to add data is through the Django admin interface.

1. **Run the server:**
   ```bash
   python manage.py runserver
   ```

2. **Access admin:** http://127.0.0.1:8000/admin

3. **Add data manually:**
   - Click on "Cities" to add cities
   - Click on "Wards" to add wards
   - Click on "Postal Codes" to add postal codes

### Option 2: Using Django Shell

```bash
python manage.py shell
```

#### Adding Cities

```python
from django_ng_locations.models import State, LGA, City

# Get the LGA
lagos_state = State.objects.get(name="Lagos")
ikeja_lga = LGA.objects.get(name="Ikeja", state=lagos_state)

# Add a city
City.objects.create(
    lga=ikeja_lga,
    name="Ikeja",
    is_capital=True,
    population=313196,
    latitude=6.5964,
    longitude=3.3425
)

# Add more cities
City.objects.create(
    lga=ikeja_lga,
    name="Alausa",
    is_capital=False
)
```

#### Adding Wards

```python
from django_ng_locations.models import LGA, Ward

# Get the LGA
ikeja_lga = LGA.objects.get(name="Ikeja", state__name="Lagos")

# Add wards
wards = [
    "Ward 1 - Anifowoshe",
    "Ward 2 - Alausa",
    "Ward 3 - Agidingbi",
    "Ward 4 - Opebi",
    "Ward 5 - Oregun",
    "Ward 6 - Ojodu",
    "Ward 7 - Omole",
    "Ward 8 - Ogba",
    "Ward 9 - Agege Motor Road",
    "Ward 10 - Oba Akran"
]

for ward_name in wards:
    Ward.objects.create(
        lga=ikeja_lga,
        name=ward_name
    )
```

#### Adding Postal Codes

```python
from django_ng_locations.models import LGA, City, PostalCode

# Get LGA and city
ikeja_lga = LGA.objects.get(name="Ikeja", state__name="Lagos")
ikeja_city = City.objects.get(name="Ikeja", lga=ikeja_lga)

# Add postal codes
PostalCode.objects.create(
    code="100001",
    lga=ikeja_lga,
    city=ikeja_city,
    area="Ikeja GRA"
)

PostalCode.objects.create(
    code="100211",
    lga=ikeja_lga,
    city=ikeja_city,
    area="Alausa"
)
```

### Option 3: Create a Custom Management Command

Create a file: `yourapp/management/commands/load_cities.py`

```python
from django.core.management.base import BaseCommand
from django_ng_locations.models import State, LGA, City

class Command(BaseCommand):
    help = 'Load city data'

    def handle(self, *args, **options):
        # Example: Load Lagos cities
        lagos = State.objects.get(name="Lagos")
        
        cities_data = {
            "Ikeja": [
                {"name": "Ikeja", "is_capital": True, "population": 313196},
                {"name": "Alausa", "is_capital": False},
                {"name": "Agidingbi", "is_capital": False},
            ],
            "Lagos Island": [
                {"name": "Lagos Island", "is_capital": False},
                {"name": "Marina", "is_capital": False},
            ],
            # Add more LGAs and cities...
        }
        
        for lga_name, cities in cities_data.items():
            lga = LGA.objects.get(name=lga_name, state=lagos)
            for city_data in cities:
                City.objects.get_or_create(
                    lga=lga,
                    name=city_data["name"],
                    defaults={
                        "is_capital": city_data.get("is_capital", False),
                        "population": city_data.get("population")
                    }
                )
                self.stdout.write(f"Created city: {city_data['name']}")
        
        self.stdout.write(self.style.SUCCESS('Successfully loaded cities'))
```

Run it:
```bash
python manage.py load_cities
```

### Option 4: Import from CSV/JSON

#### Prepare your data file (cities.csv):
```csv
lga_name,state_name,city_name,is_capital,population
Ikeja,Lagos,Ikeja,True,313196
Ikeja,Lagos,Alausa,False,
Lagos Island,Lagos,Lagos Island,False,
```

#### Create import script:

```python
import csv
from django_ng_locations.models import State, LGA, City

with open('cities.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        state = State.objects.get(name=row['state_name'])
        lga = LGA.objects.get(name=row['lga_name'], state=state)
        
        City.objects.get_or_create(
            lga=lga,
            name=row['city_name'],
            defaults={
                'is_capital': row['is_capital'].lower() == 'true',
                'population': int(row['population']) if row['population'] else None
            }
        )
```

### Option 5: Use Django Fixtures

Create a fixture file: `cities_fixture.json`

```json
[
  {
    "model": "django_ng_locations.city",
    "pk": 1,
    "fields": {
      "lga": 1,
      "name": "Ikeja",
      "is_capital": true,
      "population": 313196,
      "latitude": 6.5964,
      "longitude": 3.3425
    }
  },
  {
    "model": "django_ng_locations.city",
    "pk": 2,
    "fields": {
      "lga": 1,
      "name": "Alausa",
      "is_capital": false,
      "population": null,
      "latitude": null,
      "longitude": null
    }
  }
]
```

Load it:
```bash
python manage.py loaddata cities_fixture.json
```

## Data Sources

Here are some sources where you can find Nigerian location data:

### Cities
- Wikipedia: List of cities in Nigeria
- National Population Commission
- State government websites
- OpenStreetMap

### Wards
- Independent National Electoral Commission (INEC)
- State Independent Electoral Commissions
- Local Government websites

### Postal Codes
- Nigerian Postal Service (NIPOST)
- https://www.nipost.gov.ng

## Example: Complete Lagos State Data

Here's an example of adding complete data for Lagos State:

```python
from django_ng_locations.models import State, LGA, City, Ward, PostalCode

lagos = State.objects.get(name="Lagos")

# Add cities for each LGA
lga_cities = {
    "Ikeja": ["Ikeja", "Alausa", "Agidingbi", "Opebi", "Oregun"],
    "Lagos Island": ["Lagos Island", "Marina", "Ikoyi"],
    "Eti-Osa": ["Lekki", "Victoria Island", "Ikoyi"],
    # ... add more
}

for lga_name, cities in lga_cities.items():
    lga = LGA.objects.get(name=lga_name, state=lagos)
    for city_name in cities:
        City.objects.get_or_create(lga=lga, name=city_name)

print("Cities added successfully!")
```

## Contributing Your Data

If you've collected comprehensive data for cities, wards, or postal codes, consider:

1. **Contributing to the package**: Submit a pull request with your data
2. **Sharing as a separate package**: Create an extension package like `django-ng-locations-extended`
3. **Publishing as fixtures**: Share JSON fixtures that others can load

See [CONTRIBUTING.md](CONTRIBUTING.md) for more information.

## Tips

1. **Start small**: Add data for one state or LGA first
2. **Verify data**: Double-check accuracy before adding
3. **Use bulk_create**: For large datasets, use `bulk_create()` for better performance
4. **Backup first**: Always backup your database before bulk imports
5. **Test thoroughly**: Verify relationships are correct

## Need Help?

- Check the models in `django_ng_locations/models.py` to see available fields
- Use Django admin to see what data is already loaded
- Test with a small dataset first
- Create an issue on GitHub if you need assistance

