# Assignment 1: Design Your Own Class 

# Parent Class
class Device:
    def __init__(self, brand):
        self.brand = brand

    def info(self):
        return f"This device is made by {self.brand}."


# Child Class (Inheritance from Device)
class Smartphone(Device):
    def __init__(self, brand, model, storage, battery):
        super().__init__(brand)   # Inheriting brand from Device
        self.model = model
        self.storage = storage
        self.__battery = battery  # Encapsulation: private attribute

    # Method to display details
    def phone_info(self):
        return f"{self.brand} {self.model} with {self.storage}GB storage."

    # Getter method (Encapsulation)
    def get_battery(self):
        return f"Battery: {self.__battery}%"

    # Setter method (Encapsulation)
    def charge_battery(self, amount):
        self.__battery = min(100, self.__battery + amount)
        return f"Battery charged. Current: {self.__battery}%"


# Creating objects
phone1 = Smartphone("Apple", "iPhone 15", 256, 75)
phone2 = Smartphone("Samsung", "Galaxy S24", 512, 50)

# Using methods
print(phone1.phone_info())
print(phone1.get_battery())
print(phone1.charge_battery(20))

print(phone2.phone_info())
print(phone2.get_battery())

# Activity 2: Polymorphism Challenge 

class Car:
    def move(self):
        return "Driving"

class Plane:
    def move(self):
        return "Flying"

class Boat:
    def move(self):
        return "Sailing"

# Polymorphism in action
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())  # Same method, different behavior
