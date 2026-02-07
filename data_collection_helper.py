"""
Helper script to collect and structure Nigerian location data
This script helps you build the nested data structure for cities, wards, and postal codes
"""

import json

# Template for the data structure
TEMPLATE = {
    "Zone Name": {
        "code": "zone_code",
        "states": {
            "State Name": {
                "code": "ST",
                "capital": "Capital City",
                "lgas": {
                    "LGA Name": {
                        "cities": ["City1", "City2"],
                        "wards": ["Ward1", "Ward2", "Ward3"],
                        "postal_codes": ["100001", "100002"]
                    }
                }
            }
        }
    }
}


def add_city_to_lga(data, zone, state, lga, city_name):
    """Add a city to an LGA"""
    if "cities" not in data[zone]["states"][state]["lgas"][lga]:
        data[zone]["states"][state]["lgas"][lga]["cities"] = []
    
    if city_name not in data[zone]["states"][state]["lgas"][lga]["cities"]:
        data[zone]["states"][state]["lgas"][lga]["cities"].append(city_name)
    
    return data


def add_ward_to_lga(data, zone, state, lga, ward_name):
    """Add a ward to an LGA"""
    if "wards" not in data[zone]["states"][state]["lgas"][lga]:
        data[zone]["states"][state]["lgas"][lga]["wards"] = []
    
    if ward_name not in data[zone]["states"][state]["lgas"][lga]["wards"]:
        data[zone]["states"][state]["lgas"][lga]["wards"].append(ward_name)
    
    return data


def add_postal_code_to_lga(data, zone, state, lga, postal_code):
    """Add a postal code to an LGA"""
    if "postal_codes" not in data[zone]["states"][state]["lgas"][lga]:
        data[zone]["states"][state]["lgas"][lga]["postal_codes"] = []
    
    if postal_code not in data[zone]["states"][state]["lgas"][lga]["postal_codes"]:
        data[zone]["states"][state]["lgas"][lga]["postal_codes"].append(postal_code)
    
    return data


def convert_existing_data_to_nested(existing_data):
    """
    Convert the existing flat LGA list structure to nested structure with empty cities/wards/postal_codes
    """
    nested_data = {}
    
    for zone_name, zone_data in existing_data.items():
        nested_data[zone_name] = {
            "code": zone_data["code"],
            "states": {}
        }
        
        for state_name, state_data in zone_data["states"].items():
            nested_data[zone_name]["states"][state_name] = {
                "code": state_data.get("code", ""),
                "capital": state_data.get("capital", ""),
                "lgas": {}
            }
            
            # Convert LGA list to dict with empty arrays
            for lga_name in state_data.get("lgas", []):
                nested_data[zone_name]["states"][state_name]["lgas"][lga_name] = {
                    "cities": [],
                    "wards": [],
                    "postal_codes": []
                }
    
    return nested_data


def save_to_python_file(data, filename="django_ng_locations/fixtures/nigeria_data.py"):
    """Save data to Python file"""
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Complete Nigerian geographic data including zones, states, LGAs, cities, wards, and postal codes.\n')
        f.write('"""\n\n')
        f.write('NIGERIA_DATA = ')
        f.write(json.dumps(data, indent=4, ensure_ascii=False))
        f.write('\n')
    
    print(f"Data saved to {filename}")


def load_from_json(filename):
    """Load data from JSON file"""
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# Example usage
if __name__ == "__main__":
    print("Data Collection Helper")
    print("=" * 50)
    print("\nThis script helps you structure Nigerian location data.")
    print("\nOptions:")
    print("1. Convert existing data to nested structure")
    print("2. Add cities to LGAs")
    print("3. Add wards to LGAs")
    print("4. Add postal codes to LGAs")
    print("5. Save data to Python file")
    print("\nSee the functions above for how to use this helper.")

