MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

more_coffe = True


def check_resources(drink):
    for ingredients in MENU[drink]['ingredients']:
        if resources[ingredients] <= MENU[drink]['ingredients'][ingredients]:
            print(f"Sorry there is not enough {ingredients}.")
            return False

    return True

def deduct_resource(drink):
    for ingredient in MENU[drink]['ingredients']:
        resources[ingredient] -= MENU[drink]['ingredients'][ingredient]

def check_coins(drink):
    print("Please insert Coins")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    dollor = (quarters * 0.25) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)
    price = MENU[drink]['cost']
    if price <= dollor:
        deduct_resource(drink)
        balance = dollor - price
        global profit
        profit += price
        print(f"Here is ${round(balance,2)} in change")
        return True
    else:
        print("Sorry that's not enough money. Money refunded")
        return False


while more_coffe:

    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if drink == "espresso" or drink == "latte" or drink == "cappuccino":
        if check_resources(drink):
            if check_coins(drink):
                print(f"Here is your {drink} ☕️. Enjoy")
        else:
            more_coffe = False
    elif drink == "off":
        print("The coffee machine has been turned off")
        more_coffe = False
    elif drink == "report":
        print(f"Milk: {resources['milk']}")
        print(f"coffee: {resources['coffee']}")
        print(f"Money: {profit}")
        print(f"Water: {resources['water']}")
