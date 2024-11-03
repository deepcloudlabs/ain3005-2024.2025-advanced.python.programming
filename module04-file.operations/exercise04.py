import pickle

with open("countries.pkl", "rb") as file:
    countries = pickle.load(file)
    total = 0
    for country in countries:
        total += country[3]
        print(country)
    print(total)