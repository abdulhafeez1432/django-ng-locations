# Extended Data Collection for Django NG Locations

## Summary

This document explains how to add cities, wards, and postal codes to the `django-ng-locations` package.

## Current Status

✅ **Included:**
- 6 Geopolitical Zones
- 37 States (with codes and capitals)
- 774 LGAs

❌ **Not Included (Need to Collect):**
- Cities
- Wards  
- Postal Codes

## Files Created to Help You

### 1. `DATA_COLLECTION_GUIDE.md`
**Purpose:** Comprehensive guide on where and how to collect data

**Contents:**
- Data sources for cities, wards, and postal codes
- Collection strategies (partial vs complete)
- Realistic timelines
- Verification methods

**Start here** to understand the data collection process.

### 2. `sample_extended_data.py`
**Purpose:** Shows the exact structure you want with real examples

**Contents:**
- Sample data for Lagos State (8 LGAs)
- Sample data for Ogun State (2 LGAs)
- Sample data for Rivers State (2 LGAs)
- Proper nested structure with cities, wards, and postal codes

**Use this** as a template for structuring your data.

### 3. `convert_to_nested_structure.py`
**Purpose:** Converts existing flat data to nested structure

**How to use:**
```bash
python convert_to_nested_structure.py
```

**Output:** Creates `nigeria_data_nested.py` with all 774 LGAs in nested format with empty arrays for cities, wards, and postal codes.

**Next step:** Fill in the empty arrays with actual data.

### 4. `data_collection_helper.py`
**Purpose:** Helper functions for adding data programmatically

**Functions:**
- `add_city_to_lga()` - Add a city to an LGA
- `add_ward_to_lga()` - Add a ward to an LGA
- `add_postal_code_to_lga()` - Add a postal code to an LGA
- `convert_existing_data_to_nested()` - Convert flat to nested structure
- `save_to_python_file()` - Save data to Python file

**Use this** when you want to add data programmatically instead of manually editing files.

### 5. `postal_code_scraper_template.py`
**Purpose:** Template for collecting postal codes (manual or automated)

**Features:**
- Web scraping template (needs customization)
- Manual entry mode (interactive)
- Known postal codes for major cities (starter data)

**How to use:**
```bash
python postal_code_scraper_template.py
```

Choose option 1 to export known postal codes, or option 2 for manual entry.

## Recommended Workflow

### Option A: Quick Start with Sample Data

1. **Review the sample:**
   ```bash
   # Look at sample_extended_data.py
   ```

2. **Use sample data for testing:**
   - Copy sample data to `django_ng_locations/fixtures/nigeria_data.py`
   - Test the package with limited but complete data
   - Publish with clear documentation about coverage

3. **Expand gradually:**
   - Add more states over time
   - Accept community contributions

### Option B: Build Complete Data Gradually

1. **Convert existing data:**
   ```bash
   python convert_to_nested_structure.py
   ```
   This creates `nigeria_data_nested.py` with all 774 LGAs.

2. **Add data state by state:**
   - Open `nigeria_data_nested.py`
   - Pick a state (e.g., Lagos)
   - Add cities, wards, and postal codes for each LGA
   - Use `DATA_COLLECTION_GUIDE.md` for data sources

3. **Verify and save:**
   - Test with a few LGAs first
   - Verify data accuracy
   - Replace `django_ng_locations/fixtures/nigeria_data.py` when ready

4. **Update management command:**
   - The `load_ng_locations` command will need updates to load cities, wards, and postal codes
   - See instructions below

### Option C: Community-Driven Approach

1. **Publish current version:**
   - Release package with zones, states, and LGAs only
   - Document that cities/wards/postal codes are not included

2. **Create contribution process:**
   - Set up GitHub repository
   - Create contribution guidelines
   - Accept pull requests with verified data

3. **Build incrementally:**
   - Merge verified contributions
   - Release updates as data becomes available

## Updating the Management Command

Once you have extended data, update `django_ng_locations/management/commands/load_ng_locations.py`:

```python
# Add after loading LGAs:

# Load cities
for city_name in lga_data.get("cities", []):
    City.objects.get_or_create(
        lga=lga_obj,
        name=city_name
    )

# Load wards
for ward_name in lga_data.get("wards", []):
    Ward.objects.get_or_create(
        lga=lga_obj,
        name=ward_name
    )

# Load postal codes
for postal_code in lga_data.get("postal_codes", []):
    PostalCode.objects.get_or_create(
        lga=lga_obj,
        code=postal_code
    )
```

## Data Sources Quick Reference

### Cities
- Google Maps
- Wikipedia: "List of cities in [State]"
- State government websites

### Wards
- INEC: https://www.inecnigeria.org
- HDX: https://data.humdata.org/dataset/nigeria-independent-national-electoral-commission-lga-and-wards

### Postal Codes
- NIPOST: https://nipost.gov.ng/postcode-finder/
- Zipcode.com.ng: https://www.zipcode.com.ng/
- Use `postal_code_scraper_template.py` for known codes

## Realistic Timeline

- **1 LGA (complete data):** 30-60 minutes
- **1 State (average 20 LGAs):** 2-4 weeks
- **All 36 States + FCT:** 18-24 months (full-time)

## Recommendations

1. **Start Small:** Focus on 3-5 major states first
2. **Quality over Quantity:** Accurate data for 10 states > incomplete data for all 36
3. **Document Coverage:** Always state which areas have complete data
4. **Community Help:** Engage Nigerian developers for contributions
5. **Incremental Releases:** Update package as more data becomes available

## Next Steps

1. ✅ **Deleted `nigeria_data.json`** (already done)
2. 📖 **Read `DATA_COLLECTION_GUIDE.md`**
3. 🎯 **Decide on approach** (A, B, or C above)
4. 🚀 **Start collecting data** for your chosen states
5. 🧪 **Test with sample data** from `sample_extended_data.py`

## Questions?

- See `DATA_COLLECTION_GUIDE.md` for detailed instructions
- See `sample_extended_data.py` for data structure examples
- Run `python convert_to_nested_structure.py` to get started
- Run `python postal_code_scraper_template.py` for postal code collection

## Important Note

**Getting complete data for all 774 LGAs is a massive undertaking.** Consider:
- Publishing with partial data
- Clearly documenting coverage
- Building a community around the project
- Accepting contributions over time

This is a long-term project that will benefit from community involvement!

