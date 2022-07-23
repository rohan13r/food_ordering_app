
from re import X



"""Admin will have the following functionalities:

Add new food items. Food Item will have the following details:
FoodID //It should be generated automatically by the application.
Name
Quantity. For eg, 100ml, 250gm, 4pieces etc
Price
Discount
Stock. Amount left in stock in the restaurant.
Edit food items using FoodID.
View the list of all food items.
Remove a food item from the menu using FoodID.
"""
admin_keys = {'user':'password'}

inven = {1: {'ItemName': 'Aashirvad Ata', 'ItemID': 1, 'Price': 250, 'Stock': 14,'Quantity':'1 piece'},
        2: {'ItemName': 'Surf Excel', 'ItemID': 2, 'Price': 150, 'Stock': 20,'Quantity':'1 piece'},
        3: {'ItemName': 'Cake', 'ItemID': 3, 'Price': 300, 'Stock': 5,'Quantity':'1 piece'}}
#nested dict
## generating new id 
import random as rd
import string
def id_generator():
    code = ''.join([rd.choice(string.ascii_letters+string.digits) for n in range(7)])
    return code

def discount(price):
    discount = rd.randint(5,50)
    discounted_price = ((100 - discount)*price)/100
    return int(discounted_price)
    




def add_new_item():
    itemname = input("Enter the Item name: ")
    itemid = inven[-1]['ItemID']+1
    price = int(input("Enter the price of the item: "))
    stock = int(input("Enter the stock value of item: "))
    quantity = input('Enter the quantity')
    inven[itemid] = {
        "ItemName": itemname,
        "ItemID": itemid,
        "Price": price,
        "Stock": stock,
        'Quantity':quantity,
    }
    print("The Item"+itemname+ "is successfully added")
    return inven


    
def edit_from_item():
    item = int(input("Enter the itemid which you want to edit: "))
    a = input("Enter the item name")
    b = int(input("Enter the price of item"))
    d = int(input("Enter the stock of the item"))
    q = input('Enter the quantity of the item')
    inven[item]["ItemName"] = a
    inven[item]["Price"] = b
    inven[item]["Stock"] = d 
    inven[item]['Quantity'] = q
    print("*****Edited item successfully*****")
    return inven

def show_inven():
    print("*****HERE IS THE INVENTORY OF RAKSHAK MART*****")
    for i in inven:
        print(*inven[i].items())
        print(*inven[i].values())
        

def remove_item():
    d = int(input("Enter the Item id which you want to exit"))
    inven.pop(d)
    print("Remove item successfully ")
    return inven
