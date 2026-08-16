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
    "milk": 1000,
    "water": 2000,
    "coffee": 500,
    "money": 0
}

choose_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()

def calculate_money():
    quarters=float(input("How many quarters? "))
    dimes=float(input("How many dimes? "))
    nickels=float(input("How many nickels? "))
    pennies=float(input("How many pennies? "))
    total = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return total



def coffee(choose_coffee):
    total_money = calculate_money()
    if report["milk"] >= menu[choose_coffee]["ingredients"]["milk"] and report["water"] >= menu[choose_coffee]["ingredients"]["water"] and report["coffee"] >= menu[choose_coffee]["ingredients"]["coffee"]:
        report["milk"] -= menu[choose_coffee]["ingredients"]["milk"]
        report["water"] -= menu[choose_coffee]["ingredients"]["water"]
        report["coffee"] -= menu[choose_coffee]["ingredients"]["coffee"]
        report["money"] += menu[choose_coffee]["cost"]
        print("Here is your " + choose_coffee + " ☕. Enjoy!")
        print(f"Here is your change: ${total_money - menu[choose_coffee]['cost']:.2f}")
    else:
        print("Sorry, there are not enough resources to make a " + choose_coffee + ".")



def update_report():
    print(f"Milk: {report['milk']}ml")
    print(f"Water: {report['water']}ml")
    print(f"Coffee: {report['coffee']}g")
    print(f"Money: ${report['money']:.2f}")


continues=True

while report["milk"] > 0 and report["water"] > 0 and report["coffee"] > 0 and continues!=False:
    choose_coffee = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if choose_coffee == "espresso":
        coffee(choose_coffee)
        update_report()
    elif choose_coffee == "latte":
        coffee(choose_coffee)
        update_report()
    elif choose_coffee == "cappuccino":
        coffee(choose_coffee)
        update_report()
    elif choose_coffee == "report":
        update_report()
    else:
        print("Invalid choice. Please try again.")
        continues=False
    
        






