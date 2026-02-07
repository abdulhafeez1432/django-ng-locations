"""
Script to convert existing nigeria_data.py to nested structure with empty arrays for cities, wards, and postal codes
Run this script to prepare the data structure for adding extended data
"""

import sys
import os

# Add the django_ng_locations to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from django_ng_locations.fixtures.nigeria_data import NIGERIA_DATA


def convert_to_nested_structure(data):
    """
    Convert flat LGA list to nested structure with cities, wards, and postal_codes arrays
    """
    nested_data = {}
    
    for zone_name, zone_info in data.items():
        print(f"Processing zone: {zone_name}")
        
        nested_data[zone_name] = {
            "code": zone_info["code"],
            "states": {}
        }
        
        for state_name, state_info in zone_info["states"].items():
            print(f"  Processing state: {state_name}")
            
            nested_data[zone_name]["states"][state_name] = {
                "code": state_info.get("code", ""),
                "capital": state_info.get("capital", ""),
                "lgas": {}
            }
            
            # Convert LGA list to nested dict
            lga_list = state_info.get("lgas", [])
            lga_count = len(lga_list)
            print(f"    Converting {lga_count} LGAs...")
            
            for lga_name in lga_list:
                nested_data[zone_name]["states"][state_name]["lgas"][lga_name] = {
                    "cities": [],
                    "wards": [],
                    "postal_codes": []
                }
    
    return nested_data


def save_to_file(data, filename="nigeria_data_nested.py"):
    """Save the nested data structure to a Python file"""
    import json
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write('"""\n')
        f.write('Nigerian geographic data with nested structure for cities, wards, and postal codes.\n')
        f.write('\n')
        f.write('Structure:\n')
        f.write('- 6 Geopolitical Zones\n')
        f.write('- 37 States (with codes and capitals)\n')
        f.write('- 774 LGAs (with empty arrays for cities, wards, and postal codes)\n')
        f.write('\n')
        f.write('To add data:\n')
        f.write('1. Add cities to the "cities" array for each LGA\n')
        f.write('2. Add wards to the "wards" array for each LGA\n')
        f.write('3. Add postal codes to the "postal_codes" array for each LGA\n')
        f.write('\n')
        f.write('See sample_extended_data.py for examples of populated data.\n')
        f.write('"""\n\n')
        f.write('NIGERIA_DATA = ')
        
        # Use json.dumps for pretty formatting
        json_str = json.dumps(data, indent=4, ensure_ascii=False)
        f.write(json_str)
        f.write('\n')
    
    print(f"\n✅ Data saved to {filename}")
    print(f"\nNext steps:")
    print(f"1. Review the file: {filename}")
    print(f"2. Start adding cities, wards, and postal codes to LGAs")
    print(f"3. See sample_extended_data.py for examples")
    print(f"4. See DATA_COLLECTION_GUIDE.md for data sources")


def print_statistics(data):
    """Print statistics about the data"""
    zone_count = len(data)
    state_count = sum(len(zone["states"]) for zone in data.values())
    lga_count = sum(
        len(state["lgas"]) 
        for zone in data.values() 
        for state in zone["states"].values()
    )
    
    print("\n" + "="*60)
    print("DATA STATISTICS")
    print("="*60)
    print(f"Zones: {zone_count}")
    print(f"States: {state_count}")
    print(f"LGAs: {lga_count}")
    print("="*60)
    
    # Show breakdown by zone
    print("\nBreakdown by Zone:")
    for zone_name, zone_data in data.items():
        state_count = len(zone_data["states"])
        lga_count = sum(len(state["lgas"]) for state in zone_data["states"].values())
        print(f"  {zone_name}: {state_count} states, {lga_count} LGAs")


if __name__ == "__main__":
    print("Converting Nigeria Data to Nested Structure")
    print("="*60)
    
    # Convert the data
    nested_data = convert_to_nested_structure(NIGERIA_DATA)
    
    # Print statistics
    print_statistics(nested_data)
    
    # Save to file
    output_file = "nigeria_data_nested.py"
    save_to_file(nested_data, output_file)
    
    print("\n" + "="*60)
    print("CONVERSION COMPLETE!")
    print("="*60)
    print(f"\nThe nested structure has been saved to: {output_file}")
    print("\nYou can now:")
    print("1. Review the structure")
    print("2. Start adding cities, wards, and postal codes")
    print("3. Replace django_ng_locations/fixtures/nigeria_data.py when ready")
    print("\nSee DATA_COLLECTION_GUIDE.md for detailed instructions.")

