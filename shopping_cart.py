# shopping_cart.py

import datetime as dt
import os
from dotenv import load_dotenv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

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

# for validation process
valid_ids = []
for x in products:
    valid_ids.append(str(x["id"]))

# current date / time
checkout_time = dt.datetime.now()
checkout_time2 = checkout_time.strftime("%Y-%m-%d %I:%M %p")
subtotal = 0
product_ids = []

while True:
    product_id = input("Please input a product identifier, or 'DONE' if there are no more items: ")
    # "DONE"
    if product_id.upper() == "DONE":
        customer_email = input("Enter email for a digital copy of your receipt. Otherwise enter 'N': ")
        break
    elif product_id not in valid_ids:
        print("Hey, are you sure that product identifier is correct? Please try again!")
    else:
        product_ids.append(product_id)

# INFO DISPLAY / OUTPUT

# grocery store name and website URL
print("---------------------------------")
print("NESTLE GROCERY")
print("WWW.NESTLE-GROCERY.COM")
print("---------------------------------")
# datetime formatting - beginning of checkout process
print("CHECKOUT AT: " + checkout_time2)
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

# Sending Receipts via Email
#https: // github.com/prof-rossetti/intro-to-python/blob/main/notes/python/packages/sendgrid.md

if customer_email == "N":
    pass
else:
    SENDGRID_API_KEY = os.getenv("SENDGRID_API_KEY", default="OOPS, please set env var called 'SENDGRID_API_KEY'")
    SENDER_ADDRESS = os.getenv("SENDER_ADDRESS", default="OOPS, please set env var called 'SENDER_ADDRESS'")
    store_email = SENDER_ADDRESS

    client = SendGridAPIClient(SENDGRID_API_KEY)

    subject = "Your Receipt from Nestle Grocery Store - WWW.NESTLE-GROCERY.COM"
    content1 = "CHECKOUT AT: ", checkout_time2
    content2 = "SUBTOTAL: ", to_usd(subtotal)
    content3 = "TAX: ", to_usd(tax_total)
    content4 = "TOTAL: ", to_usd(total)
    content5 = "THANKS, SEE YOU AGAIN SOON!"
    content = content1, content2, content3, content4, content5

    message = Mail(from_email=store_email, to_emails=customer_email, subject=subject, html_content=content)

    try:
        response = client.send(message)
        # > <class 'python_http_client.client.Response'>
        print("RESPONSE:", type(response))
        print(response.status_code)  # > 202 indicates SUCCESS
        print(response.body)
        print(response.headers)

    except Exception as err:
        print(type(err))
        print(err)
