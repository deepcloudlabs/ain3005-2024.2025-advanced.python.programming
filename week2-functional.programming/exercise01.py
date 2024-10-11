import json
continents = []
with open("resources/countries.json",mode="rt",encoding="utf-8") as file:
    countries = json.load(file)
    for country in countries:
        continent = country["continent"]
        if continent not in continents:
            continents.append(continent)
continents.sort()
print(continents)