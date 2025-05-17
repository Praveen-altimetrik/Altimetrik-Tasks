from abc import ABC , abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def fuel_type(self):
        pass

class Bike(Vehicle):
    def fuel_type(self):
        print("Bike uses petrol")

class Car(Vehicle):
    def fuel_type(self):
        print("Car uses diesel and petrol")

a = Bike()
b = Car()


a.fuel_type()
b.fuel_type()
