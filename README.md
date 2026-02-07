# Django NG Locations

A comprehensive Django package for Nigerian geographic data including geopolitical zones, states, and Local Government Areas (LGAs), with models ready for cities, wards, and postal codes.

## Features

- **Complete Nigerian Geographic Data**: All 6 geopolitical zones, 36 states + FCT, and 774 LGAs
- **Extensible Models**: Ready-to-use models for cities, wards, and postal codes (data can be added)
- **Django Admin Integration**: Fully configured admin interface with search and filters
- **Utility Functions**: Helper functions for common location queries
- **Easy Data Loading**: Management command to populate your database
- **Reusable**: Can be integrated into any Django project
- **Well Documented**: Comprehensive documentation and examples

## Data Coverage

### ✅ Included Data (Ready to Use)
- **6 Geopolitical Zones** - North Central, North East, North West, South East, South South, South West
- **37 States** - All 36 states + FCT with state codes and capitals
- **774 LGAs** - All Local Government Areas

### 📋 Models Ready (Data Can Be Added)
- **Cities** - Model structure ready, you can add city data
- **Wards** - Model structure ready, you can add ward data
- **Postal Codes** - Model structure ready, you can add postal code data

## Installation

### From PyPI (when published)

```bash
pip install django-ng-locations
```

### From Source

```bash
git clone https://github.com/abdulhafeez1432/django-ng-locations.git
cd django-ng-locations
pip install -e .
```

## Quick Start

### 1. Add to Installed Apps

Add `django_ng_locations` to your `INSTALLED_APPS` in `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_ng_locations',
    ...
]
```

### 2. Run Migrations

```bash
python manage.py migrate
```

### 3. Load Nigerian Location Data

```bash
python manage.py load_ng_locations
```

To clear existing data and reload:

```bash
python manage.py load_ng_locations --clear
```

## Models

### Zone
Represents the 6 geopolitical zones of Nigeria:
- North Central
- North East
- North West
- South East
- South South
- South West

### State
Represents the 36 states of Nigeria plus FCT. Each state belongs to a zone.

### LGA (Local Government Area)
Represents the 774 Local Government Areas in Nigeria. Each LGA belongs to a state.

### City
Represents cities and towns in Nigeria. Each city belongs to an LGA.
**Note:** Model is ready, but city data is not included. You can add your own city data.

### Ward
Represents electoral/administrative wards. Each ward belongs to an LGA.
**Note:** Model is ready, but ward data is not included. You can add your own ward data.

### PostalCode
Represents postal codes in Nigeria. Each postal code is associated with an LGA and optionally a city.
**Note:** Model is ready, but postal code data is not included. You can add your own postal code data.

## Usage Examples

### Using the Models

```python
from django_ng_locations.models import Zone, State, LGA

# Get all zones
zones = Zone.objects.all()

# Get a specific state
lagos = State.objects.get(name="Lagos")

# Get all LGAs in a state
lagos_lgas = LGA.objects.filter(state=lagos)

# Get state's zone
zone = lagos.zone  # Returns "South West"

# Get all states in a zone
south_west_states = State.objects.filter(zone__name="South West")
```

### Using Utility Functions

```python
from django_ng_locations.utils import (
    get_states_by_zone,
    get_lgas_by_state,
    get_state_by_name,
    search_locations
)

# Get all states in a zone
states = get_states_by_zone("North Central")

# Get all LGAs in a state
lgas = get_lgas_by_state("Lagos")

# Get a specific state
lagos = get_state_by_name("Lagos")

# Search across all location types
results = search_locations("Ikeja")
# Returns: {'zones': [...], 'states': [...], 'lgas': [...], 'cities': [...], 'wards': [...]}
```

### In Django Forms

```python
from django import forms
from django_ng_locations.models import State, LGA

class AddressForm(forms.Form):
    state = forms.ModelChoiceField(
        queryset=State.objects.all().order_by('name')
    )
    lga = forms.ModelChoiceField(
        queryset=LGA.objects.all().order_by('name')
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Filter LGAs based on selected state
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['lga'].queryset = LGA.objects.filter(
                    state_id=state_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass
```

### In Django REST Framework

```python
from rest_framework import serializers
from django_ng_locations.models import State, LGA

class StateSerializer(serializers.ModelSerializer):
    zone_name = serializers.CharField(source='zone.name', read_only=True)
    lga_count = serializers.SerializerMethodField()
    
    class Meta:
        model = State
        fields = ['id', 'name', 'code', 'capital', 'zone_name', 'lga_count']
    
    def get_lga_count(self, obj):
        return obj.lgas.count()
```

## API Reference

### Utility Functions

All utility functions are available in `django_ng_locations.utils`:

- `get_all_zones()` - Get all geopolitical zones
- `get_zone_by_name(name)` - Get a zone by name
- `get_zone_by_code(code)` - Get a zone by code
- `get_states_by_zone(zone_name)` - Get all states in a zone
- `get_state_by_name(name)` - Get a state by name
- `get_state_by_code(code)` - Get a state by code
- `get_lgas_by_state(state_name)` - Get all LGAs in a state
- `get_lgas_by_zone(zone_name)` - Get all LGAs in a zone
- `get_lga_by_name(lga_name, state_name=None)` - Get an LGA by name
- `get_cities_by_lga(lga_name, state_name=None)` - Get all cities in an LGA
- `get_cities_by_state(state_name)` - Get all cities in a state
- `get_city_by_name(city_name, state_name=None)` - Get a city by name
- `get_wards_by_lga(lga_name, state_name=None)` - Get all wards in an LGA
- `get_wards_by_state(state_name)` - Get all wards in a state
- `get_postal_code(code)` - Get postal code information
- `get_postal_codes_by_lga(lga_name, state_name=None)` - Get postal codes in an LGA
- `get_postal_codes_by_state(state_name)` - Get postal codes in a state
- `search_locations(query)` - Search across all location types

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

Olaniyan Adewale Hafeez - support@techwareinnovation.com

## Acknowledgments

- Data sourced from official Nigerian government sources
- Built with Django

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

