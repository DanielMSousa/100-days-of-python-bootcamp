#Nesting:
#You can have many dictionary with key_value pairs inside of each other
#or even dictionaries and keys inside of a list (or vice-versa)

capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

#Nesting a list in a dictionary

travel_log = {
  "France": ['Paris', 'Lille', 'Dijon'],
  "Germany": ["Berlin", "Hamburg", "Stuttgart"]
}

["A", "B", ["C", "D"]]

travel_log = {
  "France": {"cities_visited": ['Paris', 'Lille', 'Dijon'], "total_visits": 12},
  "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
"total_visits": 5}
}

travel_log = [
  {
    "country": "France",
    "cities_visited": ['Paris', 'Lille', 'Dijon'],
    "total_visits": 12
  },
  {
    "country": "Germany", 
    "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
    "total_visits": 5
  }
]