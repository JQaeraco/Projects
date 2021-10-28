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
        """Prints 'Vroom' max_speed times"""
        print("Vroom " * self.max_speed)


class Bus(Vehicle):
    """Bus is a Vehicle that can drive humans around in it"""

    def fare(self, age: float) -> None:
        """Tells how much fare is for a particular age"""

        fare_status = ""

        if age in range(18) or 61 <= age:
            fare_status = "free"
            print(f"The fare of the bus ride is {fare_status}")
        elif age < 0:
            print("come back once you are conceived")
        else:
            fare_status = "$5"
            print(f"the fare of the bus ride is {fare_status}")


some_vehicle = Vehicle("car", 10, 5)
# some_vehicle.__init__("car", 10, 5)
some_vehicle.vroom()

some_bus = Bus("Translink Bus", 100, 35)
some_bus.fare(18)

some_bus.fare(-1)
some_bus.fare(61)
some_bus.fare(0)
some_bus.fare(17)
some_bus.fare(60)
