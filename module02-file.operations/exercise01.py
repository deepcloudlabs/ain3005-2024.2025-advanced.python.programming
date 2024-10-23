countries = [
    ("tur", "turkey", "asia", 80000000.0),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

with open("countries.txt", "wt") as file:
    for code, name, continent, population in countries:
        file.write(f"{code},{name},{continent},{population}\n")