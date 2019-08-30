from movements import *
from habitats import *

# Parakeets
# Earthworms
# Terrapins
# Timber Rattlesnake
# Mice
# Ants
# Finches
# Betta Fish
# Copperhead snake
# Gerbils

class Animal:

    def __init__(self, name, age, species):
        self.name = name
        self.age = age
        self.species = species

    def eat(self):
        print(f"The {self.species} eats food.")

class Parakeet(Animal, Waddling, Swimming):

    def __init__(self, name, age, species, wing_span, chirps_chirped):
        super().__init__(name, age, species)
        self.wing_span = wing_span
        self.chirps_chirped = chirps_chirped

class Earthworm(Animal, Digging):

    def __init__(self, name, age, species, length, dirt_devoured):
        super().__init__(name, age, species)
        self.length = length
        self.dirt_devoured = dirt_devoured

class Terrapin(Animal, Crawling):

    def __init__(self, name, age, species, shell_circumference):
        super().__init__(name, age, species)
        self.shell_circumference = shell_circumference

class Rattlesnake(Animal, Crawling):

    def __init__(self, name, age, species, rattles_rattled):
        super().__init__(name, age, species)
        self.rattles_rattled = rattles_rattled

class Rattlesnake(Animal, Slithering):

    def __init__(self, name, age, species, rattles_rattled):
        super().__init__(name, age, species)
        self.rattles_rattled = rattles_rattled

class Mouse(Animal, Crawling):

    def __init__(self, name, age, species, cheese_begot):
        super().__init__(name, age, species)
        self.cheese_begot = cheese_begot

parakeet_bob = Parakeet("Bob", 5, "Parakeet", 4, 100)
earthworm_jim = Earthworm("Jim", .1, "Earthworm", 10, 500)
terrapin_mihn = Terrapin("Mihn", .20, "Terrapin", 8)
rattlesnake_jake = Rattlesnake("Jake", .3, "Rattlesnake", 3)
mouse_krauss = Mouse("Krauss", 1, "Mouse", )
# Mice
# Ants
# Finches
# Betta Fish
# Copperhead snake
# Gerbils