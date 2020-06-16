# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Class Vehicle is the base class
class Vehicle:
    # def __init__(self, brand):
    #     self.brand = brand
    # def __str__(self):
    #     pass
    pass

class GroundVehicle(Vehicle):
    # def __init__(self, brand, wheels):
    #     super().__init__(brand)
    #     self.wheels = wheels

    # def __str__(self):
    #     pass
    pass

class FlightVehicle(Vehicle):
    # def __init__(self, brand, weight):
    #     super().__init__(brand)
    #     self.weight = weight

    # def __str__(self):
    #     pass
    pass

class Car(GroundVehicle):
    # def __init__(self, brand, wheels, engine_capacity):
    #     super().__init__(brand, wheels)
    #     self.engine_capacity = engine_capacity

    # def __str__(self):
    #     pass
    pass

class Motorcycle(GroundVehicle):
    # def __init__(self, brand, wheels, type):
    #     super().__init__(brand, wheels)
    #     self.type = type

    # def __str__(self):
    #     pass
    pass

class Airplane(FlightVehicle):
    # def __init__(self, brand, weight, capacity):
    #     super().__init__(brand, weight)
    #     self.capacity = capacity

    # def __str__(self):
    #     pass
    pass

class Starship(FlightVehicle):
    # def __init__(self, brand, weight, speed):
    #     super().__init__(brand, weight)
    #     self.speed = speed

    # def __str__(self):
    #     pass
    pass