
from typing import AsyncGenerator


class Dog():
    """A simple attempt o model a dog."""
    
    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age  = age
    
    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(self.name.title() + " is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(self.name.title() + " rolled over!")


my_dog = Dog('Watson', 3)
print("My dog's name is " + my_dog.name + ".")
print("My dog is " + str(my_dog.age) + " years old.")
my_dog.sit()
my_dog.roll_over()

class Car():
    """A simple attempt to represent a car."""
    
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
    
    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name"""
        long_name = str(self.year) + " " + self.make + " " + self.model
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print("This car has " + str(self.odometer_reading) + " miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value."""
        self.odometer_reading = mileage





my_new_car = Car('Lamborghini', 'Countach', 1985)
print(my_new_car.get_descriptive_name())
my_new_car.read_odometer()
my_new_car.odometer_reading = 3500
my_new_car.read_odometer()
my_new_car.update_odometer(1200)
my_new_car.read_odometer()
my_new_car.update_odometer(2000)
my_new_car.read_odometer()

class Battery():
    """A simple attempt to modeal a battery for an electric car."""

    def __init__(self, battery_capacity = 70):
        """Initialize the battery's attributes"""
        self.battery_capacity = battery_capacity

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print("This car has a " + str(self.battery_capacity) + "kWh battery.")

#Inheritance example
class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    def __init__(self, make, model, year):
        """Initialize attributes of the parent class.
            Then initialize attributes specific to an electric car."""
        super().__init__(make, model, year) #tells Python to call init function from parent (super) class
        self.battery = Battery()


my_tesla = ElectricCar('Tesla', 'Model X', 2023)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()

#Example of importing a class from another file
from Automobile import Automobile

my_automobile = Automobile('BMW', 'i3', 2015)
print(my_automobile.get_descriptive_name())

my_automobile.odometer_reading = 2021
my_automobile.read_odometer()