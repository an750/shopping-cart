# Shopping Cart Project

## Setup

Create a virtual environment:

```sh
conda create -n shopping-env python=3.8
```

Activate the virtual environment:
```sh
conda activate shopping-env
```

Install package dependencies:
```sh
pip install -r requirements.txt
```

## Email Setup
First, sign up for a SendGrid account, (https://signup.sendgrid.com/) then follow the instructions to complete your "Single Sender Verification", clicking the link in a confirmation email to verify your account.
Then create a SendGrid API Key with "full access" permissions.

## ".env" file

Set up a local ".env" file to configure your own tax rate, email adress, and SendGrid API Key via the environment variables: TAX_RATE, SENDER_ADDRESS, and SENDGRID_API_KEY
```sh
 # example of the ".env" file...

 TAX_RATE=0.09 #enter desired tax rate here
 SENDER_ADDRESS="myname@example.com" #enter your email
 SENDGRID_TEMPLATE_ID="ex123" #enter your own SendGrid API Key
```

## ".csv" file
To use your own custom CSV file inventory, copy the provided "data/default_products.csv" file into your local repo as "data/products.csv", where the program will be looking for it.

## Usage

Run the program:

```sh
python shopping_cart.py
```
