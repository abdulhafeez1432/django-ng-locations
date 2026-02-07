# Example Usage of Django NG Locations

This document provides detailed examples of how to use the `django-ng-locations` package in your Django projects.

## Installation in Your Project

```bash
pip install django-ng-locations
```

Add to your `settings.py`:

```python
INSTALLED_APPS = [
    ...
    'django_ng_locations',
    ...
]
```

Run migrations and load data:

```bash
python manage.py migrate
python manage.py load_ng_locations
```

## Example 1: User Profile with Location

```python
# models.py
from django.db import models
from django.contrib.auth.models import User
from django_ng_locations.models import State, LGA

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.SET_NULL, null=True)
    lga = models.ForeignKey(LGA, on_delete=models.SET_NULL, null=True)
    address = models.TextField()
    
    def __str__(self):
        return f"{self.user.username}'s Profile"
```

## Example 2: E-commerce Delivery Zones

```python
# models.py
from django.db import models
from django_ng_locations.models import State, LGA

class DeliveryZone(models.Model):
    name = models.CharField(max_length=100)
    states = models.ManyToManyField(State)
    delivery_fee = models.DecimalField(max_digits=10, decimal_places=2)
    delivery_days = models.IntegerField(help_text="Estimated delivery days")
    
    def __str__(self):
        return self.name

class Order(models.Model):
    customer_name = models.CharField(max_length=200)
    delivery_state = models.ForeignKey(State, on_delete=models.PROTECT)
    delivery_lga = models.ForeignKey(LGA, on_delete=models.PROTECT)
    delivery_address = models.TextField()
    
    def get_delivery_fee(self):
        try:
            zone = DeliveryZone.objects.get(states=self.delivery_state)
            return zone.delivery_fee
        except DeliveryZone.DoesNotExist:
            return 0
```

## Example 3: Dynamic Form with Cascading Dropdowns

```python
# forms.py
from django import forms
from django_ng_locations.models import Zone, State, LGA

class LocationForm(forms.Form):
    zone = forms.ModelChoiceField(
        queryset=Zone.objects.all(),
        required=True,
        empty_label="Select Zone"
    )
    state = forms.ModelChoiceField(
        queryset=State.objects.none(),
        required=True,
        empty_label="Select State"
    )
    lga = forms.ModelChoiceField(
        queryset=LGA.objects.none(),
        required=True,
        empty_label="Select LGA"
    )
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'zone' in self.data:
            try:
                zone_id = int(self.data.get('zone'))
                self.fields['state'].queryset = State.objects.filter(
                    zone_id=zone_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass
        
        if 'state' in self.data:
            try:
                state_id = int(self.data.get('state'))
                self.fields['lga'].queryset = LGA.objects.filter(
                    state_id=state_id
                ).order_by('name')
            except (ValueError, TypeError):
                pass

# views.py
from django.shortcuts import render
from .forms import LocationForm

def location_view(request):
    if request.method == 'POST':
        form = LocationForm(request.POST)
        if form.is_valid():
            # Process the form
            zone = form.cleaned_data['zone']
            state = form.cleaned_data['state']
            lga = form.cleaned_data['lga']
            # Do something with the data
    else:
        form = LocationForm()
    
    return render(request, 'location_form.html', {'form': form})
```

## Example 4: REST API with Django REST Framework

```python
# serializers.py
from rest_framework import serializers
from django_ng_locations.models import Zone, State, LGA

class ZoneSerializer(serializers.ModelSerializer):
    state_count = serializers.SerializerMethodField()
    
    class Meta:
        model = Zone
        fields = ['id', 'name', 'code', 'state_count']
    
    def get_state_count(self, obj):
        return obj.states.count()

class StateSerializer(serializers.ModelSerializer):
    zone_name = serializers.CharField(source='zone.name', read_only=True)
    lga_count = serializers.SerializerMethodField()
    
    class Meta:
        model = State
        fields = ['id', 'name', 'code', 'capital', 'zone', 'zone_name', 'lga_count']
    
    def get_lga_count(self, obj):
        return obj.lgas.count()

class LGASerializer(serializers.ModelSerializer):
    state_name = serializers.CharField(source='state.name', read_only=True)
    zone_name = serializers.CharField(source='state.zone.name', read_only=True)
    
    class Meta:
        model = LGA
        fields = ['id', 'name', 'code', 'state', 'state_name', 'zone_name']

# views.py
from rest_framework import viewsets, filters
from django_ng_locations.models import Zone, State, LGA
from .serializers import ZoneSerializer, StateSerializer, LGASerializer

class ZoneViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Zone.objects.all()
    serializer_class = ZoneSerializer

class StateViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = State.objects.all()
    serializer_class = StateSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'code']
    
    def get_queryset(self):
        queryset = State.objects.all()
        zone_id = self.request.query_params.get('zone', None)
        if zone_id is not None:
            queryset = queryset.filter(zone_id=zone_id)
        return queryset

class LGAViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = LGA.objects.all()
    serializer_class = LGASerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name']
    
    def get_queryset(self):
        queryset = LGA.objects.all()
        state_id = self.request.query_params.get('state', None)
        if state_id is not None:
            queryset = queryset.filter(state_id=state_id)
        return queryset

# urls.py
from rest_framework.routers import DefaultRouter
from .views import ZoneViewSet, StateViewSet, LGAViewSet

router = DefaultRouter()
router.register(r'zones', ZoneViewSet)
router.register(r'states', StateViewSet)
router.register(r'lgas', LGAViewSet)

urlpatterns = router.urls
```

## Example 5: Using Utility Functions

```python
from django_ng_locations.utils import (
    get_states_by_zone,
    get_lgas_by_state,
    search_locations
)

# Get all states in South West
south_west_states = get_states_by_zone("South West")
for state in south_west_states:
    print(f"{state.name} - Capital: {state.capital}")

# Get all LGAs in Lagos
lagos_lgas = get_lgas_by_state("Lagos")
print(f"Lagos has {lagos_lgas.count()} LGAs")

# Search for locations
results = search_locations("Ikeja")
print(f"Found {results['lgas'].count()} LGAs matching 'Ikeja'")
print(f"Found {results['cities'].count()} cities matching 'Ikeja'")
```

## Example 6: Custom Management Command

```python
# yourapp/management/commands/populate_delivery_zones.py
from django.core.management.base import BaseCommand
from django_ng_locations.models import State
from yourapp.models import DeliveryZone

class Command(BaseCommand):
    help = 'Populate delivery zones based on geopolitical zones'
    
    def handle(self, *args, **options):
        # Create delivery zones for each geopolitical zone
        zones_data = {
            'South West Zone': {'fee': 1500, 'days': 2},
            'South East Zone': {'fee': 2000, 'days': 3},
            'South South Zone': {'fee': 2500, 'days': 3},
            'North Central Zone': {'fee': 2000, 'days': 3},
            'North West Zone': {'fee': 3000, 'days': 4},
            'North East Zone': {'fee': 3500, 'days': 5},
        }
        
        for zone_name, data in zones_data.items():
            delivery_zone, created = DeliveryZone.objects.get_or_create(
                name=zone_name,
                defaults={
                    'delivery_fee': data['fee'],
                    'delivery_days': data['days']
                }
            )
            
            # Add states to this delivery zone
            geo_zone_name = zone_name.replace(' Zone', '')
            states = State.objects.filter(zone__name=geo_zone_name)
            delivery_zone.states.set(states)
            
            self.stdout.write(
                self.style.SUCCESS(
                    f"{'Created' if created else 'Updated'} {zone_name} "
                    f"with {states.count()} states"
                )
            )
```

## Tips and Best Practices

1. **Use select_related and prefetch_related** for better performance:
   ```python
   states = State.objects.select_related('zone').all()
   lgas = LGA.objects.select_related('state', 'state__zone').all()
   ```

2. **Cache frequently accessed data**:
   ```python
   from django.core.cache import cache
   
   def get_all_states():
       states = cache.get('all_states')
       if not states:
           states = list(State.objects.all())
           cache.set('all_states', states, 3600)  # Cache for 1 hour
       return states
   ```

3. **Use utility functions** instead of writing custom queries

4. **Validate location relationships** in your forms and models

5. **Consider adding indexes** if you frequently query by specific fields

