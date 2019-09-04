class Car:

    def __init__(self, manufacturer="", model="", horsepower=0, wheel_count=0):
        self.manufacturer = manufacturer
        self.model = model
        self.horsepower = horsepower
        self.wheel_count = wheel_count

class GasPowered(Car):

    def __init__(self, capacity):
        super().init(manufacturer="", model="", horsepower=0, wheel_count=0)

    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f"You used 4 gallons, you have {self.gas_level} gallons left.")

    def refuel(self):
        self.gas_level = self.fuel_capacity
        print(f"The car's gas level is now {self.gas_level}")

class ElectricPowered(Car):

    def __init__(self, manufacturer="", model="", fuel_capacity=0, gas_level=0, horsepower=0, wheel_count=0):
        self.manufacturer = manufacturer
        self.model = model
        self.fuel_capacity = fuel_capacity
        self.gas_level = gas_level
        self.horsepower = horsepower
        self.wheel_count = wheel_count

    def drive(self, lowerby):
        self.gas_level -= lowerby
        print(f"You used 4 gallons, you have {self.gas_level} gallons left.")

    def refuel(self):
        self.gas_level = self.fuel_capacity
        print(f"The car's gas level is now {self.gas_level}")

class Mustang(Car):

    def __init__(self):
        super().__init__("Mustang", "Ford", 20, 460, 4)

    def drive(self):
        super().drive(4)

    def refuel(self):
        super().refuel()

class Ram(Car):

    def __init__(self):
        super().__init__("Ram", "Dodge", 26, 395, 4)

    def drive(self):
        super().drive(5)

    def refuel(self):
        super().refuel()

class Leaf(Car):

    def __init__(self, battery_level=10, battery_capacity=20):
        super().__init__("Leaf", "Nissan", 0, 200, 4)
        self.battery_level = battery_level

    def drive(self):
        self.battery_level -= 2
        print(f"The battery level has been lowered to {self.battery_level}.")

    def recharge(self):
        battery_level = battery_capacity
        print(f"Battery level is now {battery_capacity}")

# 1. Create a Nissan Leaf class
#     * `manufacturer` attribute
#     * `model` attribute
#     * `battery_capacity` attribute
#     * `battery_level` attribute
#     * `horsepower` attribute
#     * `wheel_count` attribute
#     * `drive()` method lowers `battery_level` by 2 each time it is invoked
#     * `recharge()` method sets `battery_level` to `battery_capacity` value