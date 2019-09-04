class Moving:

    def __init__(self, movement_speed, legs):
        self.movement_speed = 0
        self.legs = 0

    def run(self):
        print("The animal walks")

class Swimming(Moving):

    def __init__(self):
        self.swim_speed = 0
        self.maximum_depth = 0

    def swim(self):
        print("The animal swims")

class Waddling(Moving):

    def __init__(self):
        self.walk_speed = 0
        self.legs = 0

    def run(self):
        print("The animal waddles")

class Digging(Moving):

    def __init__(self):
        self.dig_speed = 0
        self.legs = 0

    def run(self):
        print("The animal digs")

class Crawling(Moving):

    def __init__(self):
        self.crawl_speed = 0
        self.legs = 0

    def run(self):
        print("The animal crawls")

class Slithering(Moving):

    def __init__(self):
        self.crawl_speed = 0
        self.legs = 0

    def run(self):
        print(f"The animal slithers")

class Flying(Moving):

    def __init__(self):
        self.crawl_speed = 0
        self.legs = 0

    def run(self):
        print(f"The animal flys")