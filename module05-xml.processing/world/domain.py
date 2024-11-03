class Country:
    def __init__(self):
        self._code = ""
        self._name = ""
        self._continent = "Asia"
        self._population = 0
        self._surface_area = 0.0

    @property
    def code(self):
        return self._code

    @code.setter
    def code(self, code):
        self._code = code

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def continent(self):
        return self._continent

    @continent.setter
    def continent(self, continent):
        self._continent = continent

    @property
    def nufus(self):
        return self._population

    @nufus.setter
    def nufus(self, population):
        self._population = int(population)

    @property
    def surfaceArea(self):
        return self._surface_area

    @surfaceArea.setter
    def surfaceArea(self, surfaceArea):
        self._surface_area = float(surfaceArea)

    def __str__(self):
        return f"Country [code: {self.code}, name: {self.name}, continent: {self.continent}, population: {self.nufus}, surface area:{self.surfaceArea}]"