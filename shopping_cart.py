# shopping_cart.py

import datetime as dt
import os
from dotenv import load_dotenv

#invoking this function loads contents of the ".env" file into the script's environment
load_dotenv()

products = [
    {"id": 1, "name": "Chocolate Sandwich Cookies", "department": "snacks", "aisle": "cookies cakes", "price": 3.50},
    {"id": 2, "name": "All-Seasons Salt", "department": "pantry", "aisle": "spices seasonings", "price": 4.99},
    {"id": 3, "name": "Robust Golden Unsweetened Oolong Tea", "department": "beverages", "aisle": "tea", "price": 2.49},
    {"id": 4, "name": "Smart Ones Classic Favorites Mini Rigatoni With Vodka Cream Sauce", "department": "frozen", "aisle": "frozen meals", "price": 6.99},
    {"id": 5, "name": "Green Chile Anytime Sauce", "department": "pantry", "aisle": "marinades meat preparation", "price": 7.99},
    {"id": 6, "name": "Dry Nose Oil", "department": "personal care", "aisle": "cold flu allergy", "price": 21.99},
    {"id": 7, "name": "Pure Coconut Water With Orange", "department": "beverages", "aisle": "juice nectars", "price": 3.50},
    {"id": 8, "name": "Cut Russet Potatoes Steam N' Mash", "department": "frozen", "aisle": "frozen produce", "price": 4.25},
    {"id": 9, "name": "Light Strawberry Blueberry Yogurt", "department": "dairy eggs", "aisle": "yogurt", "price": 6.50},
    {"id": 10, "name": "Sparkling Orange Juice & Prickly Pear Beverage", "department": "beverages", "aisle": "water seltzer sparkling water", "price": 2.99},
    {"id": 11, "name": "Peach Mango Juice", "department": "beverages", "aisle": "refrigerated", "price": 1.99},
    {"id": 12, "name": "Chocolate Fudge Layer Cake", "department": "frozen", "aisle": "frozen dessert", "price": 18.50},
    {"id": 13, "name": "Saline Nasal Mist", "department": "personal care", "aisle": "cold flu allergy", "price": 16.00},
    {"id": 14, "name": "Fresh Scent Dishwasher Cleaner", "department": "household", "aisle": "dish detergents", "price": 4.99},
    {"id": 15, "name": "Overnight Diapers Size 6", "department": "babies", "aisle": "diapers wipes", "price": 25.50},
    {"id": 16, "name": "Mint Chocolate Flavored Syrup", "department": "snacks", "aisle": "ice cream toppings", "price": 4.50},
    {"id": 17, "name": "Rendered Duck Fat", "department": "meat seafood", "aisle": "poultry counter", "price": 9.99},
    {"id": 18, "name": "Pizza for One Suprema Frozen Pizza", "department": "frozen", "aisle": "frozen pizza", "price": 12.50},
    {"id": 19, "name": "Gluten Free Quinoa Three Cheese & Mushroom Blend", "department": "dry goods pasta", "aisle": "grains rice dried goods", "price": 3.99},
    {"id": 20, "name": "Pomegranate Cranberry & Aloe Vera Enrich Drink", "department": "beverages", "aisle": "juice nectars", "price": 4.25}
]  # based on data from Instacart: https://www.instacart.com/datasets/grocery-shopping-2017

def to_usd(my_price):
    """
    Converts a numeric value to usd-formatted string, for printing and display purposes.
    """
    return f"${my_price:,.2f}"  # > $12,000.71

# INFO CAPTURE / INPUT

# current date / time
checkout_time = dt.datetime.now()
subtotal = 0
product_ids = []

while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    # "DONE"
    if product_id == "DONE":
        break
    else:
        product_ids.append(product_id)

# INFO DISPLAY / OUTPUT

# grocery store name and website URL
print("---------------------------------")
print("NESTLE GROCERY")
print("WWW.NESTLE-GROCERY.COM")
print("---------------------------------")
# datetime formatting - beginning of checkout process
print("CHECKOUT AT: " + checkout_time.strftime("%Y-%m-%d %I:%M %p"))
print("---------------------------------")
print("SELECTED PRODUCTS:")

# name and price of each shopping cart item
for product_id in product_ids:
    matching_products = [p for p in products if str(p["id"]) == str(product_id)]
    matching_product = matching_products[0]
    subtotal = subtotal + matching_product["price"]
    print(" ... " + matching_product["name"] + " (" + to_usd(matching_product["price"]) + ")")

# calculate taxes
tax_rate = float(os.getenv("TAX_RATE", default=".0875"))
tax_total = subtotal * tax_rate

# total cost
total = subtotal + tax_total

print("---------------------------------")
print("SUBTOTAL: " + to_usd(subtotal))
print("TAX: " + to_usd(tax_total))
print("TOTAL: " + to_usd(total))
print("---------------------------------")
# friendly message
print("THANKS, SEE YOU AGAIN SOON!")
print("---------------------------------")
