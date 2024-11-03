import json
from functools import reduce


def hist_reducer(histogram, continent):
    if continent not in histogram:
        histogram[continent] = 0
    histogram[continent] += 1
    return histogram


with open("resources/countries.json", mode="rt", encoding="utf-8") as file:
    countries = json.load(file)
    solution = reduce(hist_reducer, map(lambda country: country["continent"], countries), {})
    sorted_solution = sorted(solution.items(), key=lambda x: x[0], reverse=True)
    print(solution)
    print(sorted_solution)
