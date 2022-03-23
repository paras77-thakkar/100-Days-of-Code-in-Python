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
money=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
def is_resource_sufficient(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"​Sorry there is not enough {item}.")
            return False
    return True
def payment():
    print("Please Insert Coins")
    quarters=int(input("How Many Quarters?:"))*0.25
    dimes=int(input("How Many Dimes?:"))*0.1
    nickles=int(input("How Many Nickles?:"))*0.05
    pennies=int(input("How many pennies?"))*0.01
    total=quarters+dimes+nickles+pennies
    return total

def transaction_successful(pay,drink_cost):
        if pay>=drink_cost:
            change=round(pay-drink_cost,2)
            print(f"Your change is ${change}")
            global money
            money+=drink_cost
            return True
        else:
            print("Sorry you haven't paid enough money,money will be refunded")
            return False
def order_coffee(drink,drink_ingredients):
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Your {drink} is Ready ")

on= True
while on:
    user_input= input("What would you like? (espresso/latte/cappuccino):").lower()
    if user_input == "off":
        on=False
    elif user_input == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Water: {resources['coffee']}ml")
        print(f"Money: ${money}")
    else:
        drink=MENU[user_input]
        if is_resource_sufficient(drink["ingredients"]):
            pay=payment()
            if transaction_successful(pay, drink["cost"]):
                order_coffee(user_input, drink["ingredients"])
