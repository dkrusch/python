import datetime

class Building:

    def __init__(self, address, stories):
        self.designer = "Daniel Krusch"
        self.date_constructed = ""
        self.owner = ""
        self.address = address
        self.stories = stories

    def construct(self):
        self.date_constructed = datetime.datetime.now()

    def purchase(self, new_owner):
        self.owner = new_owner

    def describe_building(self):
        print(f"{self.address} was purchased by {self.owner} on {self.date_constructed:%m/%d/%Y} and has {self.stories} stories.")
        # for attribute, value in self.__dict__.items():
        #     print(f"{attribute}: {value}")

big_building = Building("800 8th Street", 12)
big_building.construct()
big_building.purchase("Bob")
big_building.describe_building()