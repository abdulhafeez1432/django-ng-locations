# Data Collection Guide for Cities, Wards, and Postal Codes

## Overview

This guide helps you collect and structure data for Nigerian cities, wards, and postal codes to extend the `django-ng-locations` package.

## Current Status

✅ **Complete Data:**
- 6 Geopolitical Zones
- 37 States (with codes and capitals)
- 774 LGAs

❌ **Missing Data (Need to Collect):**
- Cities for each LGA
- Wards for each LGA
- Postal codes for each LGA

## Data Sources

### 1. Cities Data

**Online Sources:**
- Wikipedia: Search for "List of cities in [State Name]"
- Google Maps: Browse each LGA to find major cities/towns
- State Government Websites
- OpenStreetMap: https://www.openstreetmap.org

**Recommended Approach:**
- Start with state capitals and major cities
- Add at least the LGA headquarters for each LGA
- Add other significant towns/areas

### 2. Wards Data

**Official Source:**
- INEC (Independent National Electoral Commission)
- Website: https://www.inecnigeria.org
- Download: Electoral ward boundaries data

**Alternative Sources:**
- State Independent Electoral Commissions (SIECs)
- Local Government websites
- HDX Dataset: https://data.humdata.org/dataset/nigeria-independent-national-electoral-commission-lga-and-wards

**Note:** The HDX dataset has ward data for some states but not all.

### 3. Postal Codes

**Official Source:**
- NIPOST (Nigerian Postal Service)
- Website: https://nipost.gov.ng/postcode-finder/
- Website: https://www.zipcode.com.ng/

**Challenges:**
- Not all areas have assigned postal codes
- Some LGAs share postal codes
- Data is not available in bulk download format

**Recommended Approach:**
- Collect postal codes for major cities first
- Use NIPOST website to search by location
- Document postal code ranges for each LGA

## Data Collection Strategy

### Phase 1: Major Cities (Recommended Start)

Focus on the 36 state capitals + FCT and major cities:

1. Lagos State (all 20 LGAs)
2. Kano State
3. Rivers State (Port Harcourt)
4. Kaduna State
5. Oyo State (Ibadan)
6. FCT (Abuja)

### Phase 2: State by State

Work through each state systematically:
- Collect data for all LGAs in one state before moving to the next
- Start with your home state or states you're familiar with

### Phase 3: Community Contribution

- Publish the package with partial data
- Encourage community contributions
- Accept pull requests with verified data

## Tools and Scripts

### 1. Using the Data Collection Helper

```python
from data_collection_helper import convert_existing_data_to_nested, save_to_python_file
from django_ng_locations.fixtures.nigeria_data import NIGERIA_DATA

# Convert existing data to nested structure
nested_data = convert_existing_data_to_nested(NIGERIA_DATA)

# Now you can manually add cities, wards, and postal codes
# Example: Add cities to Ikeja LGA in Lagos
nested_data["South West"]["states"]["Lagos"]["lgas"]["Ikeja"]["cities"] = [
    "Ikeja", "Alausa", "Agidingbi", "Opebi", "Oregun"
]

# Add wards
nested_data["South West"]["states"]["Lagos"]["lgas"]["Ikeja"]["wards"] = [
    "Anifowoshe/Ikeja", "Alausa", "Agidingbi", "Opebi", "Oregun"
]

# Add postal codes
nested_data["South West"]["states"]["Lagos"]["lgas"]["Ikeja"]["postal_codes"] = [
    "100001", "100211", "100242"
]

# Save to file
save_to_python_file(nested_data)
```

### 2. Web Scraping (Advanced)

If you're comfortable with web scraping, you can create scripts to extract data from:
- NIPOST website for postal codes
- Wikipedia for cities
- Google Maps API for locations

### 3. Manual Entry Template

Create a spreadsheet with columns:
- Zone
- State
- LGA
- City
- Ward
- Postal Code

Then convert to the nested structure using a script.

## Realistic Expectations

### Complete Data Collection Timeline

- **1 State (average 20 LGAs)**: 2-4 weeks
- **All 36 States + FCT**: 18-24 months (full-time effort)

### Recommended Approach

**Option A: Partial Release**
1. Complete data for 5-10 major states
2. Release package with partial data
3. Clearly document which states have complete data
4. Accept community contributions

**Option B: Framework First**
1. Release with zones, states, and LGAs only (current status)
2. Provide clear documentation on how users can add their own data
3. Create a separate repository for community-contributed data
4. Merge verified contributions over time

**Option C: Crowdsourcing**
1. Create a web form for data submission
2. Implement verification process
3. Build data incrementally with community help

## Sample Data Structure

See `sample_extended_data.py` for examples of properly structured data for:
- Lagos State (8 LGAs with complete data)
- Ogun State (2 LGAs with complete data)
- Rivers State (2 LGAs with complete data)

## Data Verification

Before adding data, verify:

1. **Cities**: Cross-reference with Google Maps
2. **Wards**: Verify with INEC data
3. **Postal Codes**: Confirm with NIPOST website

## Next Steps

### Immediate (This Week)

1. Review `sample_extended_data.py`
2. Decide on your data collection strategy (A, B, or C above)
3. If choosing partial data, select 3-5 states to focus on

### Short Term (This Month)

1. Collect data for selected states
2. Use `data_collection_helper.py` to structure the data
3. Test with the management command

### Long Term (3-6 Months)

1. Release package with available data
2. Document data coverage clearly
3. Set up contribution process
4. Build community around the project

## Important Notes

1. **Quality over Quantity**: Better to have accurate data for 10 states than incomplete/incorrect data for all 36

2. **Document Coverage**: Always clearly state which LGAs have complete data

3. **Version Control**: Use git to track data additions

4. **Community Input**: Nigerian developers can help verify and contribute data

5. **Incremental Updates**: Release new versions as more data becomes available

## Resources

- INEC: https://www.inecnigeria.org
- NIPOST: https://nipost.gov.ng
- HDX Nigeria Data: https://data.humdata.org/group/nga
- Wikipedia: https://en.wikipedia.org/wiki/List_of_Nigerian_cities_by_population
- OpenStreetMap: https://www.openstreetmap.org

## Questions?

If you need help with:
- Data collection strategies
- Scripting/automation
- Data verification
- Community building

Feel free to ask!

