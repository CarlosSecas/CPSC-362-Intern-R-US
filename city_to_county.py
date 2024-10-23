# dictionary to map cities with corresponding counties
city_to_county = {
    # Orange County cities
    "Irvine": "Orange County",
    "Anaheim": "Orange County",
    "Santa Ana": "Orange County",
    "Brea": "Orange County",
    "Buena Park": "Orange County",
    "Costa Mesa": "Orange County",
    "Fountain Valley": "Orange County",
    "Fullerton": "Orange County",
    "Garden Grove": "Orange County",
    "Huntington Beach": "Orange County",
    "Laguna Beach": "Orange County",
    "Laguna Hills": "Orange County",
    "Laguna Niguel": "Orange County",
    "Lake Forest": "Orange County",
    "Mission Viejo": "Orange County",
    "Newport Beach": "Orange County",
    "Orange": "Orange County",
    "San Clemente": "Orange County",
    "Tustin": "Orange County",
    "Westminster": "Orange County",
    "Yorba Linda": "Orange County",

    # Los Angeles County cities
    "Pasadena": "Los Angeles County",
    "Los Angeles": "Los Angeles County",
    "Burbank": "Los Angeles County",
    "Venice": "Los Angeles County",
    "Santa Monica": "Los Angeles County",
    "Long Beach": "Los Angeles County",
    "Glendale": "Los Angeles County",
    "Compton": "Los Angeles County",
    "Torrance": "Los Angeles County",
    "Hawthorne": "Los Angeles County",
    "Inglewood": "Los Angeles County",
    "Culver City": "Los Angeles County",
    "Downey": "Los Angeles County",
    "Whittier": "Los Angeles County",
    "Palmdale": "Los Angeles County",
    "Lancaster": "Los Angeles County"
}

# Function to get county from city
def get_county_from_city(city):
    for key in city_to_county:
        if key in city:
            return city_to_county[key]
    return "Unknown County"  # For cities not in the dictiona