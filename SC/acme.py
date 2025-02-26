from random import randint


class Product:
    """Class for products"""
    def __init__(self, name, price=10, weight=20, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = identifier

    def stealability(self):
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        elif ratio >= 0.5 and ratio < 1:
            return "Kinda stealable."
        else:
            return "Very stealable!"

    def explode(self):
        hazard = self.flammability * self.weight
        if hazard < 10:
            return "...fizzle."
        elif hazard >= 10 and hazard < 50:
            return "...boom!"
        else:
            return "...BABOOM!"


class BoxingGlovea(Product):
    def __init__(self, name=None, price=10, weight=10, flammability=0.5,
                 identifier=randint(1000000, 10000000)):
            super().__init__(name, price, weight, flammability, identifier)

    def explod(self):
        return "...it's a glove."

    def punch(self):
        if self.weight < 5:
            return "That tickles."
        elif self.weight >= 5 and self.weight < 15:
            return "Hey, that hurt!"
        else:
            return "OUCH!"
