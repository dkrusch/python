class Arrangement:

    def __init__(self):
        self.__flowers = []

    def enhance(self, flower):
        self.__flowers.append(flower)


class MothersDay(Arrangement):

    def __init__(self):
        super().__init__()

    # Override the `enhance` method to ensure only
    # roses, lillies, and alstroemeria can be added


class ValentinesDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        try:
            if flower.pesticides_used > -1:
                print(f"You added a {flower.pedal_color} flower to the arrangement")
                flower.stem_length = 7
                super().enhance(flower)
        except AttributeError as ex:
            print(f"Sorry, {flower.pedal_color} flowers just don't belong because they are organic.")

class MothersDay(Arrangement):
    def __init__(self):
        super().__init__()

    def enhance(self, flower):
        try:
            if flower.fertilizer_used > -1:
                print(f"You added a {flower.pedal_color} flower to the arrangement")
                flower.stem_length = 4
                super().enhance(flower)
        except AttributeError as ex:
            print(f"Sorry, {flower.pedal_color} flowers just don't belong.")


