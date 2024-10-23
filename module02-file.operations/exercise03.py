import pickle

countries = [
    ("tur", "turkey", "asia", 80000000.0),
    ("fra", "france", "europe", 67000000),
    ("ita", "italy", "europe", 60000000)
]

with open("countries.pkl", "wb") as file:
    pickle.dump(countries, file)