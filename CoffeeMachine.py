MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "cash": 0.00,
}

def main():
    run = True

    while run:
        choice = input("What would you like? (espresso/latte/cappuccino/report/refill/exit): ")

        if choice == "report":
            print(f"Water: {resources['water']}\nMilk: {resources['milk']}\nCoffee: {resources['coffee']}\nMoney: {resources['cash']}")
        if choice == "exit":
            print("Thank you for using the Coffee Machine. Goodbye.")
            run = False
        if choice == "espresso":
            money_check = coins('espresso')
            res_check = brew_req('espresso')
            if money_check == True and res_check == True:
                print("Here is your espresso.")
        if choice == "latte":
            money_check = coins('latte')
            res_check = brew_req('latte')
            if money_check == True and res_check == True:
                print("Here is your latte.")
        if choice == "cappuccino":
            money_check = coins('cappuccino')
            res_check = brew_req('cappuccino')
            if money_check == True and res_check == True:
                print("Here is your cappuccino.")
        if choice == "refill":
            resources['water'] = 300
            resources['milk'] = 200
            resources['coffee'] = 100

def coins(Size):
    enough_money = False
    print(f"Cost: ${MENU[Size]['cost']}")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input(f"How many nickels? "))
    pennies = int(input(f"How many pennies? "))
    money = round (float ((quarters * 0.25) + (dimes * 0.10) + (nickels + 0.05) + (pennies * 0.01) - 1), 2)
    print(f"Money given: ${money}\nCost: ${MENU[Size]['cost']}")
    if money >= int(MENU[Size]['cost']):
        enough_money = True
        change = round(money - int(MENU[Size]['cost']), 2)
        resources['cash'] += MENU[Size]['cost']
        print(f"Here is your change ${change}.")
    else:
        print("Not enough money")
    return enough_money

def brew_req(Size):
    requirements_met = False
    water = False
    milk= False
    coffee = False

    if MENU[Size]['ingredients']['water'] <= resources['water']:
        water = True
    if MENU[Size]['ingredients']['milk'] <= resources['milk']:
        milk = True
    if MENU[Size]['ingredients']['coffee'] <= resources['coffee']:
        coffee = True

    if water == True and milk == True and coffee == True:
        requirements_met = True
        print("Machine requirements met: Brewing your coffee!")

    if requirements_met == True:
        resources['water'] -= MENU[Size]['ingredients']['water']
        resources['milk'] -= MENU[Size]['ingredients']['milk']
        resources['coffee'] -= MENU[Size]['ingredients']['coffee']

    return requirements_met


main()