# Activity 1: Design Your Own Class: Smartphone

class Smartphone:
    def __init__(self, brand, model, storage_gb, battery_life_hours):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.battery_life_hours = battery_life_hours

    def make_call(self, number):
        print(f"Calling {number} using {self.brand} {self.model}...")

    def charge(self):
        print(f"Charging {self.brand} {self.model}... Battery life is {self.battery_life_hours} hours when fully charged.")


# Inheritance example: adding a subclass with extra features
class SmartCameraPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, battery_life_hours, camera_megapixels):
        super().__init__(brand, model, storage_gb, battery_life_hours)
        self.camera_megapixels = camera_megapixels

    def take_photo(self):
        print(f"Taking photo with {self.camera_megapixels}MP camera on {self.brand} {self.model}.")


# Activity 2: Polymorphism Challenge with Vehicle classes

class Vehicle:
    def move(self):
        pass


class Car(Vehicle):
    def move(self):
        print("Driving 🚗")


class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")


class Boat(Vehicle):
    def move(self):
        print("Sailing 🚤")


# Testing all classes:

# Activity 1
phone = Smartphone("Apple", "iPhone 14", 128, 20)
phone.make_call("123-456-7890")
phone.charge()

camera_phone = SmartCameraPhone("Samsung", "Galaxy S23 Ultra", 256, 22, 108)
camera_phone.take_photo()
camera_phone.make_call("098-765-4321")

# Activity 2
vehicles = [Car(), Plane(), Boat()]
for v in vehicles:
    v.move()

