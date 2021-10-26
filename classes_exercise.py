# classes_exercise.py

"""
1. Create a class according to the following requirements:
It's name is Vehicle and it has the following attributes/methods:
Attributes/properties:
  name: str
  max_speed: int
  capacity: int
Methods:
    vroom() -> None
        Prints "Vroom" max_speed times
2. Create a child/subclass of Vehicle called Bus with the following methods:
Methods:
    fare(age: float) -> None
        Prints "The fare of the bus ride is {}."
            Price depends on age:
                0-17 years - Free
                18-60 years - $5
                61+ years - Free
"""

class Vehicle:
    """
    name: str
    max_speed: int
    capacity: int
    """

    def __init__(self, name: str, max_speed: int, capacity: int):
        self.name = name
        self.max_speed = max_speed
        self.capacity = capacity


    def vroom(self) -> None:
        return "Vroom " * self.max_speed

class Bus(Vehicle):
    def fare(self, age: float) -> None:

        if age in range(18) or 61 <= age:
            print("The fare of the bus ride is free")
        elif age < 0:
            print("come back once you are conceived")
        else:
            print("the fare of the bus ride is $5")


some_vehicle = Vehicle("car", 10, 5)
# some_vehicle.__init__("car", 10, 5)
print(some_vehicle.vroom())

some_bus = Bus("car", 10, 5)
print(some_bus.fare(18))
print(some_bus.fare(1))
print(some_bus.fare(-1))
print(some_bus.fare(62))

