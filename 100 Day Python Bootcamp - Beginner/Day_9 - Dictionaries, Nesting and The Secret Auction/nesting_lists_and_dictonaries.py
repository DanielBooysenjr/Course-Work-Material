

# Nesting Lists and Dictionaries

# Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}

# Nesting a list in a dictonary

# travel_log = {
#     "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "Total_Visits": 12},
#     "Germany": ["Berline,", "Hamburg", "Stuttgart"],
# }

# print(travel_log)
# Nesting Dictonay in Dictonary

my_travel_log = {
    "Equatorial Guinea": {"Cities_Visited": ["Malabo"]},
    "Namibia": {"Cities_Visited": ["Windhoek"]},
    "Malta": {"Cities_Visited": ["Bugibba", "Birkirkarra", "Silema"]},
    "Etopia": {"Cities_Visited": ["Main City"]},
}

# Listing a dictonary in a list

travel_log = [
    {
        "Country": "France", 
        "cities_visited": ["Paris", "Lille", "Dijon"], 
        "Total_Visits": 12
    },
    {
        "Country": "Germany", 
        "cities_visited": ["Berline,", "Hamburg", "Stuttgart"], 
        "Total_Visits": 4
    },
]
