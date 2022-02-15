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

## ".env" file

Set up local ".env" file to configure your own tax rate via an environment variable called TAX_RATE
```sh
 # example of the ".env" file...
 TAX_RATE=0.09 #enter tax rate here
```

## Usage

Run the program:

```sh
python shopping_cart.py
```
