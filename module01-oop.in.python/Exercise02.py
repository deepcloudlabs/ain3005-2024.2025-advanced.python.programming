from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
    WHITE = 4
    BLACK = 5


class OverCapacityError(Exception):
    """
    Business Exception
    OverCapacityError is an Exception
    OverCapacityError: subclass/derived class
    Exception: super class/base class
    Raised when an over-capacity error is encountered.
    """

    def __init__(self, message: str, over_weight: float):
        super().__init__()
        self.message = message
        self.__over_weight = over_weight

    @property
    def over_weight(self):
        return self.__over_weight

    def __str__(self) -> str:
        return f'OverCapacityError [{self.message}]: {self.over_weight}'


class vehicle:
    """
            members:
            1. attributes         -> licence_plate, capacity, load, color
            2. (business) methods -> load, unload, constructor (__init__) -> create object
                                     getter/setter
                                     __str__: def __str__ object -> str
    """

    def __init__(self, licence_plate: str, capacity: float = 3_000, color: Color = Color.BLACK):
        self.__licence_plate = licence_plate
        self.__capacity = capacity
        self.__color = color
        self.__load = 0

    @property
    def capacity(self):
        return self.__capacity

    @property
    def license_plate(self):
        return self.__licence_plate

    @property
    def color(self):
        return self.__color

    @color.setter
    def color(self, color: Color):
        self.__color = color

    @property
    def current_load(self):
        return self.__load

    def load(self, weight: float) -> float:
        if weight <= 0.0:
            raise ValueError('weight must be greater than zero')
        if weight + self.__load > self.__capacity:
            raise OverCapacityError(f"{self.__load} and {weight} exceeds the capacity {self.__capacity}",
                                    self.__load + weight - self.__capacity)
        self.__load += weight
        return self.__load

    def unload(self, weight: float) -> float:
        print(f"unloading the weight ({weight}) from the vehicle ({self.__licence_plate})")
        if weight <= 0.0:
            raise ValueError('weight must be greater than zero')
        if weight > self.__load:
            raise ValueError('weight must be less than or equal to load')
        self.__load -= weight
        return self.__load

    def __str__(self):
        return f"vehicle[license_plate={self.__licence_plate}, color= {self.__color}, current load= {self.current_load}, capacity={self.__capacity}]"


vehicle1 = vehicle(licence_plate="34abc42", capacity=5_000, color=Color.RED)
vehicle2 = vehicle("06def49", 2_500, color=Color.GREEN)
vehicle3 = vehicle(capacity=8_000, licence_plate="07mn108", color=Color.BLUE)
try:
    vehicle2.load(1_000)
    vehicle3.load(2_000)
    print(f"vehicle1's current load: {vehicle1.current_load}")
    vehicle1.load(weight=500)
    print(f"vehicle1's current load: {vehicle1.current_load}")
    vehicle1.load(weight=1_500)
    print(f"vehicle1's current load: {vehicle1.current_load}")
    vehicle1.load(weight=2_000)
    print(f"vehicle1's current load: {vehicle1.current_load}")
    vehicle1.color = Color.GREEN
    vehicle1.load(weight=1_500)
    print(f"vehicle1's current load: {vehicle1.current_load}")
    print(vehicle1)  # F7BE<__main__.vehicle object at 0x0000020876B0>
    print(str(vehicle1))
except OverCapacityError as oce:
    print(oce)
except ValueError as ve:
    print(ve)
finally:
    print(f"unload all loads from vehicle1: {vehicle1.unload(vehicle1.current_load)}")
    print(f"unload all loads from vehicle2: {vehicle2.unload(vehicle2.current_load)}")
    print(f"unload all loads from vehicle3: {vehicle3.unload(vehicle3.current_load)}")
