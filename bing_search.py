#!/usr/bin/python

"""
bing_search.py: Use Bing to randomly search about Airports or EK 380 flights.
"""

import random
import time
import webbrowser

SEARCH_MAX = 4
BING_URL = "https://www.bing.com/"
SEARCH_URL = "https://www.bing.com/search?q="
AIRPORTS = [
    "Chennai/Madras (MAA)",
    "Dubai (DXB)",
    "New York, NY (JFK)",
    "Raleigh-Durham, NC (RDU)",
    "Las Vegas, NV (LAS)",
    "San Jose, CA (SJC)",
    "Columbus, OH (CMH)",
    "Baltimore, MD (BWI)",
    "Washington Dulles, VA (IAD)",
    "Philadelphia, PA (PHL)",
    "Atlanta, GA (ATL)",
    "Trenton, NJ (TTN)",
    "Abu Dhabi (AUH)",
    "Denver, CO (DEN)",
    "San Francisco, CA (SFO)",
    "Hyderabad (HYD)",
    "Goa (GOI)",
    "Dallas, TX (DFW)",
    "Doha (DOH)",
    "Bangalore (BLR)",
    "Chicago, MI (ORD)",
    "Paris (CDG)",
    "London (LHR)",
    "Hamburg (HAM)",
]

A380_FLIGHTS = [
    "Dubai-Amsterdam EK147",
    "Amsterdam-Dubai EK148",
    "Dubai-Bangkok EK384",
    "Bangkok-Dubai EK385",
    "Dubai-Beijing EK306",
    "Beijing-Dubai EK307",
    "Dubai-Jeddah EK803",
    "Jeddah-Dubai EK804",
    "Dubai-Jeddah EK805",
    "Jeddah-Dubai EK806",
    "Dubai-Bangkok-Hong Kong EK384",
    "Hong Kong-Bangkok-Dubai EK385",
    "Dubai-Hong Kong EK380",
    "Hong Kong-Dubai EK381",
    "Dubai-Hong Kong EK382",
    "Hong Kong-Dubai EK383",
    "Dubai-Johannesburg EK761",
    "Johannesburg-Dubai EK762",
    "Dubai-Kuala Lumpur EK346",
    "Kuala Lumpur-Dubai EK347",
    "Dubai-London Heathrow EK001",
    "London Heathrow-Dubai EK002",
    "Dubai-London Heathrow EK003",
    "London Heathrow-Dubai EK004",
    "Dubai-London Heathrow EK005",
    "London Heathrow-Dubai EK006",
    "Dubai-London Heathrow EK007",
    "London Heathrow-Dubai EK008",
    "Dubai-London Heathrow EK029",
    "London Heathrow-Dubai EK030",
    "Dubai-Manchester EK017",
    "Manchester-Dubai EK018",
    "Dubai-Melbourne-Auckland EK406",
    "Auckland-Melbourne-Dubai EK407",
    "Dubai-Moscow EK131",
    "Moscow-Dubai EK132",
    "Dubai-Munich EK049",
    "Munich-Dubai EK050",
    "Dubai-New York JFK EK201",
    "New York JFK-Dubai EK202",
    "Dubai-New York JFK EK203",
    "New York JFK-Dubai EK204",
    "Dubai-Paris EK073",
    "Paris-Dubai EK074",
    "Dubai-Paris EK075",
    "Paris-Dubai EK076",
    "Dubai-Rome EK97",
    "Rome-Dubai EK98",
    "Dubai-Seoul EK322",
    "Seoul-Dubai EK323",
    "Dubai-Shanghai EK302",
    "Shanghai-Dubai EK303",
    "Dubai-Singapore EK354",
    "Singapore-Dubai EK355",
    "Dubai-Sydney-Auckland EK412",
    "Auckland-Sydney-Dubai EK413",
    "Dubai-Sydney EK414",
    "Sydney-Dubai EK415",
    "Dubai-Tokyo EK318",
    "Tokyo-Dubai EK319",
    "Dubai-Toronto EK241",
    "Toronto-Dubai EK242",
    "Dubai-Zurich EK087",
    "Zurich-Dubai EK088",
] 

def bing_search(search_list):
    num_searches = 0
    bing_query_url = BING_URL + "search?q="

    while num_searches < SEARCH_MAX:
        search_term = random.choice(search_list)
        query = bing_query_url + search_term.replace(" ", "%20")
        webbrowser.open_new_tab(query)
        num_searches += 1
        time.sleep(1)

if "__main__" == __name__:
    webbrowser.open(BING_URL, new=1, autoraise=True)
    if random.choice([True, False]) is True:
        bing_search(AIRPORTS)
    else:
        bing_search(A380_FLIGHTS)
