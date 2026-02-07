"""
Utility functions for django_ng_locations
"""
from typing import Optional, List
from django.db.models import QuerySet
from .models import Zone, State, LGA, City, Ward, PostalCode


def get_all_zones() -> QuerySet:
    """Get all geopolitical zones"""
    return Zone.objects.all()


def get_zone_by_name(name: str) -> Optional[Zone]:
    """Get a zone by name"""
    try:
        return Zone.objects.get(name__iexact=name)
    except Zone.DoesNotExist:
        return None


def get_zone_by_code(code: str) -> Optional[Zone]:
    """Get a zone by code"""
    try:
        return Zone.objects.get(code__iexact=code)
    except Zone.DoesNotExist:
        return None


def get_states_by_zone(zone_name: str) -> QuerySet:
    """Get all states in a specific zone"""
    return State.objects.filter(zone__name__iexact=zone_name)


def get_state_by_name(name: str) -> Optional[State]:
    """Get a state by name"""
    try:
        return State.objects.get(name__iexact=name)
    except State.DoesNotExist:
        return None


def get_state_by_code(code: str) -> Optional[State]:
    """Get a state by code"""
    try:
        return State.objects.get(code__iexact=code)
    except State.DoesNotExist:
        return None


def get_lgas_by_state(state_name: str) -> QuerySet:
    """Get all LGAs in a specific state"""
    return LGA.objects.filter(state__name__iexact=state_name)


def get_lgas_by_zone(zone_name: str) -> QuerySet:
    """Get all LGAs in a specific zone"""
    return LGA.objects.filter(state__zone__name__iexact=zone_name)


def get_lga_by_name(lga_name: str, state_name: Optional[str] = None) -> Optional[LGA]:
    """
    Get an LGA by name, optionally filtered by state
    """
    try:
        if state_name:
            return LGA.objects.get(name__iexact=lga_name, state__name__iexact=state_name)
        return LGA.objects.get(name__iexact=lga_name)
    except (LGA.DoesNotExist, LGA.MultipleObjectsReturned):
        return None


def get_cities_by_lga(lga_name: str, state_name: Optional[str] = None) -> QuerySet:
    """Get all cities in a specific LGA"""
    if state_name:
        return City.objects.filter(lga__name__iexact=lga_name, lga__state__name__iexact=state_name)
    return City.objects.filter(lga__name__iexact=lga_name)


def get_cities_by_state(state_name: str) -> QuerySet:
    """Get all cities in a specific state"""
    return City.objects.filter(lga__state__name__iexact=state_name)


def get_city_by_name(city_name: str, state_name: Optional[str] = None) -> Optional[City]:
    """Get a city by name, optionally filtered by state"""
    try:
        if state_name:
            return City.objects.get(name__iexact=city_name, lga__state__name__iexact=state_name)
        return City.objects.get(name__iexact=city_name)
    except (City.DoesNotExist, City.MultipleObjectsReturned):
        return None


def get_wards_by_lga(lga_name: str, state_name: Optional[str] = None) -> QuerySet:
    """Get all wards in a specific LGA"""
    if state_name:
        return Ward.objects.filter(lga__name__iexact=lga_name, lga__state__name__iexact=state_name)
    return Ward.objects.filter(lga__name__iexact=lga_name)


def get_wards_by_state(state_name: str) -> QuerySet:
    """Get all wards in a specific state"""
    return Ward.objects.filter(lga__state__name__iexact=state_name)


def get_postal_code(code: str) -> Optional[PostalCode]:
    """Get postal code information"""
    try:
        return PostalCode.objects.get(code=code)
    except PostalCode.DoesNotExist:
        return None


def get_postal_codes_by_lga(lga_name: str, state_name: Optional[str] = None) -> QuerySet:
    """Get all postal codes in a specific LGA"""
    if state_name:
        return PostalCode.objects.filter(lga__name__iexact=lga_name, lga__state__name__iexact=state_name)
    return PostalCode.objects.filter(lga__name__iexact=lga_name)


def get_postal_codes_by_state(state_name: str) -> QuerySet:
    """Get all postal codes in a specific state"""
    return PostalCode.objects.filter(lga__state__name__iexact=state_name)


def search_locations(query: str) -> dict:
    """
    Search across all location types
    Returns a dictionary with matching zones, states, LGAs, cities, and wards
    """
    return {
        "zones": Zone.objects.filter(name__icontains=query),
        "states": State.objects.filter(name__icontains=query),
        "lgas": LGA.objects.filter(name__icontains=query),
        "cities": City.objects.filter(name__icontains=query),
        "wards": Ward.objects.filter(name__icontains=query),
    }

