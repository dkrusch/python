class Boat:

    def __init__(self, name=""):
        self.name = name

    def move(self, method="normally"):
        print(f"The boat: {self.name}, moves {method}")

class Kayak(Boat):

    def __init__(self, name="", kayak="yes"):
        super().__init__(name)
        self.kayak = kayak

    def paddle(self):
        self.move("paddilingly")

new_kayak = Kayak("Ayak")
new_kayak.paddle()


