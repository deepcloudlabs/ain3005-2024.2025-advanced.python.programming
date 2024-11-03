from abc import ABC, abstractmethod


# interface
class pet(ABC):  # interface
    @abstractmethod
    def play(self) -> None:
        pass

    @abstractmethod
    def set_name(self, name: str) -> None:
        pass

    @abstractmethod
    def get_name(self) -> str:
        pass


# abstract class
class animal(ABC):
    def __init__(self, legs: int) -> None:
        self.__legs = legs

    @property
    def legs(self) -> int:
        return self.__legs

    # concrete method
    def walk(self) -> None:
        print(f"Animal with {self.legs} legs is walking now...")

    @abstractmethod
    def eat(self) -> None:
        pass


class spider(animal):
    def __init__(self):
        super().__init__(8)

    def eat(self) -> None:
        print("Spider is eating now...")


class cat(animal, pet):
    def __init__(self, name: str = "Tekir"):
        super().__init__(4)
        self.__name = name

    @property
    def name(self) -> str:
        return self.__name

    def eat(self) -> None:
        print(f"{self.name} is eating now...")

    def play(self) -> None:
        print(f"{self.name} is playing now...")

    def set_name(self, name: str) -> None:
        self.__name = name

    def get_name(self) -> str:
        return self.name


zoo_animals: list[animal] = [spider(), cat("Garfield"), cat(), spider()]

for a_animal in zoo_animals:
    a_animal.walk()
    a_animal.eat()
    if isinstance(a_animal, pet):
        a_animal.play()
