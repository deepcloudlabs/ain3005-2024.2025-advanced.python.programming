import json

with open("resources/movies.json", mode="rt", encoding="utf-8") as file:
    movies = json.load(file)
    comedyMoviesFrom70s = list(filter(lambda movie: any([genre["name"] == "Comedy" for genre in movie["genres"]]) , filter(lambda movie: movie["year"] < 1980,filter(lambda movie: movie["year"] >= 1970, movies))))
    for movie in comedyMoviesFrom70s:
        print(movie["title"], movie["year"],list(map(lambda genre: genre["name"], movie["genres"])))