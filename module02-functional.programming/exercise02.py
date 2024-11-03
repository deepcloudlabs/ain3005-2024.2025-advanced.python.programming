import json
from collections.abc import Set
from functools import reduce

def continent_reducer(set_of_continents,continent):
    if continent not in set_of_continents:
        set_of_continents.append(continent)
    return set_of_continents

with open("resources/countries.json",mode="rt",encoding="utf-8") as file:
    countries = json.load(file)
    continents = reduce(continent_reducer,
                        map(lambda country: country["continent"],countries),
                        [])
continents.sort()
print(continents)