import json

with open("resources/countries.json",mode="rt",encoding="utf-8") as file:
    countries = json.load(file)
    number_of_countries = sum(map(lambda country: 1,countries))
    print(number_of_countries)