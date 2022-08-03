travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"]
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"]
    },
]


# 🚨 Do NOT change the code above

# TODO: Write the function that will allow new countries
# to be added to the travel_log. 👇

# country_name = input("Which country you want to add?")
# visits_number = input("How namy times you were there?")
# cities_visited = input("Which cities did you visit?")

def add_new_country(country_visited, times_visits, cities_visited):
    new_country = {}
    new_country["country"] = country_visited
    new_country["visits"] = times_visits
    new_country["cities"] = cities_visited
    travel_log.append(new_country)


# 🚨 Do not change the code below
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)




