"""
Sample data showing the extended structure with cities, wards, and postal codes
This is a SAMPLE for Lagos State only - you'll need to collect data for other states

Data sources used for this sample:
- Cities: Major known cities/areas in each LGA
- Wards: INEC electoral wards (sample - not complete)
- Postal Codes: NIPOST postal codes (sample - not complete)
"""

SAMPLE_NIGERIA_DATA = {
    "South West": {
        "code": "south_west",
        "states": {
            "Lagos": {
                "code": "LA",
                "capital": "Ikeja",
                "lgas": {
                    "Ikeja": {
                        "cities": ["Ikeja", "Alausa", "Agidingbi", "Opebi", "Oregun", "Ojodu", "Omole", "Ogba"],
                        "wards": [
                            "Anifowoshe/Ikeja",
                            "Alausa",
                            "Agidingbi",
                            "Opebi",
                            "Oregun",
                            "Ojodu",
                            "Omole Phase 1",
                            "Omole Phase 2",
                            "Ogba",
                            "Oba Akran"
                        ],
                        "postal_codes": ["100001", "100211", "100242", "100271", "100281"]
                    },
                    "Lagos Island": {
                        "cities": ["Lagos Island", "Marina", "Ikoyi", "Victoria Island"],
                        "wards": [
                            "Sandgrouse",
                            "Olowogbowo",
                            "Iduntafa",
                            "Idumota",
                            "Oko-Awo",
                            "Iga Iduganran",
                            "Isale Eko",
                            "Adeniji Adele",
                            "Ikoyi",
                            "Obalende"
                        ],
                        "postal_codes": ["101001", "101241", "101245", "101283"]
                    },
                    "Eti-Osa": {
                        "cities": ["Lekki", "Victoria Island", "Ikoyi", "Ajah", "Epe"],
                        "wards": [
                            "Ilasan",
                            "Ikate",
                            "Iru/Victoria Island",
                            "Igbo-Efon",
                            "Ise/Ibeju",
                            "Badore",
                            "Okunraiye",
                            "Ajah",
                            "Sangotedo",
                            "Abijo"
                        ],
                        "postal_codes": ["101245", "101283", "105102", "105104"]
                    },
                    "Alimosho": {
                        "cities": ["Ikotun", "Egbeda", "Idimu", "Igando", "Iyana Ipaja"],
                        "wards": [
                            "Ikotun/Igando I",
                            "Ikotun/Igando II",
                            "Egbe/Idimu I",
                            "Egbe/Idimu II",
                            "Ayobo/Ipaja I",
                            "Ayobo/Ipaja II",
                            "Alimosho I",
                            "Alimosho II",
                            "Mosan/Okunola I",
                            "Mosan/Okunola II",
                            "Agbado/Oke-Odo I"
                        ],
                        "postal_codes": ["100276", "102213", "102215"]
                    },
                    "Surulere": {
                        "cities": ["Surulere", "Yaba"],
                        "wards": [
                            "Coker/Aguda",
                            "Ijeshatedo/Itire",
                            "Adeniran Ogunsanya",
                            "Shitta/Bode Thomas",
                            "Iponri",
                            "Ojuelegba",
                            "Akerele",
                            "Igbobi/Jibowu",
                            "Yaba",
                            "Somolu"
                        ],
                        "postal_codes": ["101283", "100252", "100001"]
                    },
                    "Apapa": {
                        "cities": ["Apapa", "Ajegunle", "Kirikiri"],
                        "wards": [
                            "Apapa I",
                            "Apapa II",
                            "Apapa III",
                            "Apapa IV",
                            "Apapa V",
                            "Olodi",
                            "Ajegunle",
                            "Kirikiri",
                            "Suru Alaba",
                            "Tolu"
                        ],
                        "postal_codes": ["102273", "102101"]
                    },
                    "Oshodi-Isolo": {
                        "cities": ["Oshodi", "Isolo", "Ejigbo", "Okota"],
                        "wards": [
                            "Oshodi I",
                            "Oshodi II",
                            "Isolo I",
                            "Isolo II",
                            "Ejigbo",
                            "Okota",
                            "Ajao Estate",
                            "Mafoluku",
                            "Ire Akari",
                            "Ilasa"
                        ],
                        "postal_codes": ["100001", "102214"]
                    },
                    "Kosofe": {
                        "cities": ["Ketu", "Ikosi", "Oworonshoki", "Anthony"],
                        "wards": [
                            "Agboyi I",
                            "Agboyi II",
                            "Ikosi I",
                            "Ikosi II",
                            "Oworonshoki I",
                            "Oworonshoki II",
                            "Ketu",
                            "Anthony",
                            "Ojota",
                            "Alapere"
                        ],
                        "postal_codes": ["100242", "100268"]
                    }
                }
            },
            "Ogun": {
                "code": "OG",
                "capital": "Abeokuta",
                "lgas": {
                    "Abeokuta South": {
                        "cities": ["Abeokuta", "Ake", "Ijaye"],
                        "wards": [
                            "Ake I",
                            "Ake II",
                            "Ijaye",
                            "Itoko",
                            "Kemta",
                            "Ago Oba",
                            "Isale Igbein",
                            "Ijaiye Kukudi",
                            "Ita Oshin",
                            "Totoro"
                        ],
                        "postal_codes": ["110001", "110101"]
                    },
                    "Ado-Odo/Ota": {
                        "cities": ["Ota", "Sango", "Iju", "Agbara"],
                        "wards": [
                            "Ota I",
                            "Ota II",
                            "Ota III",
                            "Sango",
                            "Iju",
                            "Agbara",
                            "Ado-Odo I",
                            "Ado-Odo II",
                            "Ketu-Adie Owe",
                            "Ere"
                        ],
                        "postal_codes": ["112101", "112104"]
                    }
                }
            }
        }
    },
    "South South": {
        "code": "south_south",
        "states": {
            "Rivers": {
                "code": "RI",
                "capital": "Port Harcourt",
                "lgas": {
                    "Port Harcourt": {
                        "cities": ["Port Harcourt", "Diobu", "Rumuola"],
                        "wards": [
                            "Diobu I",
                            "Diobu II",
                            "Nkpolu/Oroworukwo",
                            "Rumuola",
                            "Rumueme",
                            "Rumuokwuta",
                            "Amadi-Ama",
                            "Mgbuoba",
                            "Elelenwo",
                            "Rumuobiakani"
                        ],
                        "postal_codes": ["500001", "500211", "500272"]
                    },
                    "Obio-Akpor": {
                        "cities": ["Rumuokoro", "Choba", "Alakahia", "Rumuigbo"],
                        "wards": [
                            "Rumuokoro",
                            "Rumueme",
                            "Rumuola",
                            "Rumuigbo",
                            "Choba",
                            "Alakahia",
                            "Ozuoba",
                            "Rumuokwurusi",
                            "Rumuodomaya",
                            "Rumuepirikom"
                        ],
                        "postal_codes": ["500101", "500102"]
                    }
                }
            }
        }
    }
}

# Note: This is SAMPLE data for demonstration purposes
# You will need to collect complete data for all 774 LGAs from various sources

