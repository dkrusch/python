class Vehicle:
    def __init__(self, color, occupancy):
        self.main_color = color
        self.maximum_occupancy = occupancy

    def drive(self):
        print("Z-ooooooooooom.")

# Electric motorcycle
class Zero(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        ...

    def drive(self):
        print("Zerooooooooooom.")

# Propellor light aircraft
class Cessna(Vehicle):
    def __init__(self, main_color, maximum_occupancy, fuel_capacity):
        super().__init__(main_color, maximum_occupancy)
        self.fuel_capacity = fuel_capacity

    def refuel_tank(self):
        ...

    def drive(self):
        print(f"The {super(Cessna, self).__self__.main_color} Cessna drives past wrrrrrrrrrrrrrrrrr. It's maxixum occupancy is {super(Cessna, self).__self__.maximum_occupancy} and its fuel capacity is {super(Cessna, self).__self__.maximum_occupancy} gallons.")

# Electric car
class Tesla(Vehicle):
    def __init__(self):
        self.battery_kwh = 0

    def charge_battery(self):
        ...

    def drive(self):
        print(". . .")

# Gas powered truck
class Ram(Vehicle):
    def __init__(self):
        self.fuel_capacity = 0

    def refuel_tank(self):
        ...

    def drive(self):
        print("Rooooooooooom.")


plane = Cessna("blue", 3, 4)
plane.drive()
steero = Zero()
steero.drive()
tes = Tesla()
tes.drive()
rom = Ram()
rom.drive()