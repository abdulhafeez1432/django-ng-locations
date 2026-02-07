"""
Template for scraping postal codes from Nigerian postal code websites
This is a TEMPLATE - you'll need to customize it based on the actual website structure

Requirements:
    pip install requests beautifulsoup4

Note: Always respect website terms of service and robots.txt
Consider adding delays between requests to avoid overloading servers
"""

import requests
from bs4 import BeautifulSoup
import time
import json


class PostalCodeScraper:
    """
    Template class for scraping Nigerian postal codes
    Customize the methods based on the actual website structure
    """
    
    def __init__(self):
        self.base_url = "https://www.zipcode.com.ng"  # Example
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    def get_postal_codes_for_state(self, state_name):
        """
        Get all postal codes for a state
        This is a TEMPLATE - customize based on actual website structure
        """
        # Example URL structure - adjust based on actual website
        url = f"{self.base_url}/{state_name.lower().replace(' ', '-')}"
        
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            
            soup = BeautifulSoup(response.content, 'html.parser')
            
            # TODO: Customize these selectors based on actual website HTML
            # This is just an example structure
            postal_codes = {}
            
            # Example: Find all LGA sections
            lga_sections = soup.find_all('div', class_='lga-section')  # Adjust selector
            
            for section in lga_sections:
                lga_name = section.find('h3').text.strip()  # Adjust selector
                codes = [code.text.strip() for code in section.find_all('span', class_='postal-code')]
                postal_codes[lga_name] = codes
            
            return postal_codes
            
        except Exception as e:
            print(f"Error fetching data for {state_name}: {e}")
            return {}
    
    def scrape_all_states(self, states_list):
        """
        Scrape postal codes for all states
        """
        all_data = {}
        
        for state in states_list:
            print(f"Scraping {state}...")
            postal_codes = self.get_postal_codes_for_state(state)
            all_data[state] = postal_codes
            
            # Be respectful - add delay between requests
            time.sleep(2)
        
        return all_data
    
    def save_to_json(self, data, filename="postal_codes.json"):
        """Save scraped data to JSON file"""
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=4, ensure_ascii=False)
        print(f"Data saved to {filename}")


# Manual data entry helper
def manual_postal_code_entry():
    """
    Helper function for manual postal code entry
    Use this if web scraping is not feasible
    """
    print("Manual Postal Code Entry")
    print("="*60)
    print("Enter postal codes for each LGA")
    print("Type 'done' when finished with an LGA")
    print("Type 'quit' to exit")
    print("="*60)
    
    data = {}
    
    while True:
        state = input("\nEnter state name (or 'quit'): ").strip()
        if state.lower() == 'quit':
            break
        
        if state not in data:
            data[state] = {}
        
        while True:
            lga = input(f"  Enter LGA name in {state} (or 'done'): ").strip()
            if lga.lower() == 'done':
                break
            
            postal_codes = []
            while True:
                code = input(f"    Enter postal code for {lga} (or 'done'): ").strip()
                if code.lower() == 'done':
                    break
                postal_codes.append(code)
            
            data[state][lga] = postal_codes
            print(f"    ✅ Added {len(postal_codes)} postal codes for {lga}")
    
    # Save to file
    with open('manual_postal_codes.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4, ensure_ascii=False)
    
    print("\n✅ Data saved to manual_postal_codes.json")
    return data


# Known postal codes for major cities (starter data)
KNOWN_POSTAL_CODES = {
    "Lagos": {
        "Ikeja": ["100001", "100211", "100242", "100271", "100281"],
        "Lagos Island": ["101001", "101241", "101245", "101283"],
        "Eti-Osa": ["101245", "101283", "105102", "105104"],
        "Surulere": ["101283", "100252", "100001"],
        "Apapa": ["102273", "102101"],
        "Alimosho": ["100276", "102213", "102215"],
        "Oshodi-Isolo": ["100001", "102214"],
        "Kosofe": ["100242", "100268"],
    },
    "Kano": {
        "Kano Municipal": ["700001", "700211", "700221"],
        "Nassarawa": ["700001"],
    },
    "Rivers": {
        "Port Harcourt": ["500001", "500211", "500272"],
        "Obio-Akpor": ["500101", "500102"],
    },
    "FCT": {
        "Abuja Municipal": ["900001", "900211", "900252", "900271"],
        "Gwagwalada": ["902101"],
        "Kuje": ["905101"],
    },
    "Ogun": {
        "Abeokuta South": ["110001", "110101"],
        "Ado-Odo/Ota": ["112101", "112104"],
    }
}


def export_known_postal_codes():
    """Export known postal codes to JSON"""
    with open('known_postal_codes.json', 'w', encoding='utf-8') as f:
        json.dump(KNOWN_POSTAL_CODES, f, indent=4, ensure_ascii=False)
    print("✅ Known postal codes exported to known_postal_codes.json")


if __name__ == "__main__":
    print("Postal Code Collection Tool")
    print("="*60)
    print("\nOptions:")
    print("1. Export known postal codes (starter data)")
    print("2. Manual entry mode")
    print("3. Web scraping mode (requires customization)")
    print("="*60)
    
    choice = input("\nSelect option (1-3): ").strip()
    
    if choice == "1":
        export_known_postal_codes()
    elif choice == "2":
        manual_postal_code_entry()
    elif choice == "3":
        print("\nWeb scraping mode requires customization.")
        print("Please review the PostalCodeScraper class and customize it")
        print("based on the actual website structure you want to scrape from.")
        print("\nRecommended websites:")
        print("- https://www.zipcode.com.ng/")
        print("- https://nipost.gov.ng/postcode-finder/")
    else:
        print("Invalid option")

