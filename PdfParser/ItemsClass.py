import json

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
         return json.dumps(self.__dict__)