class City():

    def __init__(self, name="", buildings=[], mayor="", year="0000"):
        self.name = name
        self.mayor = mayor
        self.buildings = buildings
        self.year = year

    def destroy_city(self):
        print(f"{self.name} city run by mayor {self.mayor} has been destroyed.")

    def add_building(self, building):
        self.buildings.append(building)
