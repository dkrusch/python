class Flower:

    def __init__(self, pedal_color, num_of_pedals, stem_length, organically_grown):
        self.pedal_color = pedal_color
        self.num_of_pedals = num_of_pedals
        self.stem_length = stem_length
        self.organically_grown = organically_grown


class Rose(Flower):

    def __init__(self, pedal_color, num_of_pedals, stem_length, organically_grown, pesticides_used=11):
        super().__init__(pedal_color, num_of_pedals, stem_length, organically_grown)
        self.pesticides_usedped = pesticides_used

class Daisy(Flower):

    def __init__(self, pedal_color, num_of_pedals, stem_length, organically_grown, fertilizer_used=11):
        super().__init__(pedal_color, num_of_pedals, stem_length, organically_grown)
        self.fertilizer_used = fertilizer_used

