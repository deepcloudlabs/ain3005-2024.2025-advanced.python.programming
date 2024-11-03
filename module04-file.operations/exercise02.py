with open("countries.txt", "rt") as countries:
    total = 0
    for line in countries:
        try:
            code, name, continent, population = line.strip().split(",")
            print(f"{code},{name},{continent},{population}")
            print(type(population))
            total = total + float(population)
        except ValueError as ve:
            print(f"Cannot parse {line}: {ve}")
    print(total)