menu={
    "espresso": {
        "ingredients": {
            "milk": 100,
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "milk": 150,
            "water": 200,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "milk": 100,
            "water": 250,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

report={
    "milk": 300,
    "water": 300,
    "coffee": 100,
    "money": 0
}

quarters=float(input("How many quarters? "))
dimes=float(input("How many dimes? "))
nickels=float(input("How many nickels? "))
pennies=float(input("How many pennies? "))

def calculate_money(quarters, dimes, nickels, pennies):
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total

#def prepare_latte()