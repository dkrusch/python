from building import Building, big_building
from city import City

# Name of the city.
# The mayor of the city.
# Year the city was established.
# A collection of all of the buildings in the city.
# A method to add a building to the city.

megalopolis = City()

# Awesome code here

for building in megalopolis.buildings:
    print(building)

megalopolis.name = "Big Town"
megalopolis.city = ["Wuts up"]
megalopolis.mayor = "Bob Jones"
megalopolis.year = "1815"

small_building = Building("700 7th Street", 13)
small_building.construct()
small_building.purchase("Cob")

megalopolis.add_building(small_building)
megalopolis.add_building(big_building)
megalopolis.destroy_city()
for building in megalopolis.buildings:
    print(building.address)