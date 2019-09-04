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
        Animal.__init__(self, name, age, species)
        self.wing_span = wing_span
        self.chirps_chirped = chirps_chirped

class Earthworm(Animal, Digging):

    def __init__(self, name, age, species, length, dirt_devoured):
        Animal.__init__(self, name, age, species)
        self.length = length
        self.dirt_devoured = dirt_devoured

class Terrapin(Animal, Crawling):

    def __init__(self, name, age, species, shell_circumference):
        Animal.__init__(self, name, age, species)
        self.shell_circumference = shell_circumference

class Rattlesnake(Animal, Crawling):

    def __init__(self, name, age, species, rattles_rattled):
        Animal.__init__(self, name, age, species)
        self.rattles_rattled = rattles_rattled

class Rattlesnake(Animal, Slithering):

    def __init__(self, name, age, species, rattles_rattled):
        Animal.__init__(self, name, age, species)
        self.rattles_rattled = rattles_rattled

class Mouse(Animal, Crawling):

    def __init__(self, name, age, species, cheese_begot):
        Animal.__init__(self, name, age, species)
        self.cheese_begot = cheese_begot

class Ant(Animal, Crawling):

    def __init__(self, name, age, species, mandibles):
        Animal.__init__(self, name, age, species)
        self.mandibles = mandibles

class Finch(Animal, Flying):

    def __init__(self, name, age, species, flaps):
        Animal.__init__(self, name, age, species)
        self.flaps = flaps

class BettaFish(Animal, Swimming):

    def __init__(self, name, age, species, gulps):
        Animal.__init__(self, name, age, species)
        self.gulps = gulps

class CopperheadSnake(Animal, Slithering):

    def __init__(self, name, age, species, bites_bitten):
        Animal.__init__(self, name, age, species)
        self.bites_bitten = bites_bitten

class Gerbil(Animal, Crawling):

    def __init__(self, name, age, species, spins):
        Animal.__init__(self, name, age, species)
        self.spins = spins

parakeet_bob = Parakeet("Bob", 5, "Parakeet", 4, 100)
earthworm_jim = Earthworm("Jim", .1, "Earthworm", 10, 500)
terrapin_mihn = Terrapin("Mihn", .20, "Terrapin", 8)
rattlesnake_jake = Rattlesnake("Jake", .3, "Rattlesnake", 3)
mouse_krauss = Mouse("Krauss", 1, "Mouse", 4)
mouse_lant = Ant("Lant", 1, "Ant", 2)
finch_zynch = Finch("Zynch", 1, "Finch", 2000)
betta_annetta = BettaFish("Annetta", 1, "Betta", 50)
copper_hopper = CopperheadSnake("Hopper", 1, "Copperhead", 50)
gerbil_vergil = Gerbil("Gerbil", 1, "Gerbil", 40)
gerbil_vergil.run()