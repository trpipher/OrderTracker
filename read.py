import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer

fd = open("order.pdf", "rb")
doc = PDFDocument(fd)
numpages=len([p for p in doc.pages()])
viewer = SimplePDFViewer(fd)
strings = []
for num in range(0, numpages):
    viewer.navigate(num+1)
    viewer.render()
    strings += viewer.canvas.strings

print(strings)

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
        return f'Count: {self.count} \nName: {self.name} \nFlavor: {self.flavor} \nRequests: {self.request} \nAddition: {self.addition} \nPrice: {self.price} \nPortion: {self.portion} \nSides: {self.sides}\n'

prev = ""
Items = []
item = Item()
Order = {"Items": Items, "Customer": "", "Date": "", "Total": ""}
requesting = False
for s in strings:
    if s == "x":
        Items.append(item)
        item = Item()
        item.count = prev
        prev = "x"
        requesting == False
    elif prev == "x":
        item.name = s
        prev = "name"
        requesting == False
    elif prev == "name":
        item.price = s
        prev = "price"
        requesting == False
    elif "Portion of Protein" in prev:
        item.portion = s
        prev = "portion"
        requesting == False
    elif "Sides" in prev:
        item.sides = s
        prev = "veggies"
        requesting == False
    elif "Additions" in prev:
        item.addition = s
        prev = "flavor"
        requesting == False
    elif "Special" in prev:
        item.request = s
        prev = "request"
    else:
        prev = s
Items = Items[1:]

print(Items)