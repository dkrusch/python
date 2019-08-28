class Pizza:

    def __init__(self, attributes):
        self.size = attributes["size"]
        self.style = attributes["style"]
        self.toppings = attributes["toppings"]

    def add_topping(self, topping):
        self.toppings.append(topping)

    def describe_pizza(self):
        for key, attributes in self.__dict__.items():
            print(f"{key.capitalize()}: {attributes}")

    def order_pizza(self):
        toppings_string = ""
        for i, toppings in enumerate(self.toppings):
            if i < len(self.toppings) - 2:
                toppings_string += toppings + ", "
            elif i == len(self.toppings) - 2:
                toppings_string += toppings + ", and "
            else:
                toppings_string += toppings

        print(f"I would like a {self.size}-inch, {self.style}, pizza, with {toppings_string}.")

cool_pizza = Pizza({"size": 16, "style": "Stuffed Crust", "toppings": ["mushrooms", "onions", "pepperoni"]})

cool_pizza.describe_pizza()
cool_pizza.add_topping("chicken")
cool_pizza.describe_pizza()
cool_pizza.order_pizza()