import pdfreader
from pdfreader import PDFDocument, SimplePDFViewer
from functions import cleanString
from ItemsClass import Item
from datetime import datetime
import json
import re

fd = open("order1.pdf", "rb")
doc = PDFDocument(fd)
numpages=len([p for p in doc.pages()])
viewer = SimplePDFViewer(fd)
strings = []
for num in range(0, numpages):
    viewer.navigate(num+1)
    viewer.render()
    strings += viewer.canvas.strings[4:]

print(strings)

prev = ""
Items = []
item = Item()
Order = {"Items": [], "Request": "", "Total": "","Customer": "", "Delivery": ""}
requesting = False
for s in strings:
    if s == "x":
        Items.append(item.__dict__)
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
    elif "Special requests:" in prev:

        if prev[len(prev)-1] == " ":
            item.request = cleanString(s)
            prev = "request"
        else:
            Order["Request"] = cleanString(s)
            prev = "OrderReq"
    elif "Subtotal" in s:
        Items.append(item.__dict__)
        print()
        item = Item()
        prev = s
    elif "request" in prev and not s.isnumeric():
        item.request += cleanString(s)
        prev = "request"
    elif "OrderReq" in prev:
        Order["Request"] += cleanString(s)
        prev = "OrderReq"
    elif "Total" in prev:
        Order["Total"] = s
        prev = "Num"
    elif "Num" in prev:
        Order["Customer"] = s
        prev = "Customer"
    elif "arrival" in prev:
        prev = "Instr"
    elif "Instr" in prev:
        Order["Delivery"] = s
        prev = "Delivery"
    else:
        prev = s
Order["Items"] = Items[1:]

date = re.findall('[0-9]{2}/[0-9]{2}/[0-9]{4}', Order["Delivery"])[0]
day = datetime.strptime(date,'%m/%d/%Y').strftime("%A")

Order["Delivery"] = f'{day} {date}'

print(json.dumps(Order))