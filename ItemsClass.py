class Item():
    def __init__(self):
        self.count = ""
        self.name = ""
        self.flavor = ""
        self.request = ""
        self.addition = ""
        self.price = ""
        self.portion = ""
        self.sides = ""

    def __repr__(self):
        return f'\nCount: {self.count} Name: {self.name} Flavor: {self.flavor} Requests: {self.request} Addition: {self.addition} Price: {self.price} Portion: {self.portion} Sides: {self.sides}'