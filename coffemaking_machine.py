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
profit=0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def checkResources(orderItem):
    for item in orderItem:
        if orderItem[item] > resources[item]:
            print(f"Sorry there is not enough : {item}")
            return False
        
    return True

def processcoin():
    print("Please insert the coins:")
    total=int(input("How many quater: ")) * 0.25
    total+=int(input("How many dimes: ")) * 0.10
    total+=int(input("How many nickles: ")) * 0.05
    total+=int(input("How many pennies: ")) * 0.01

    return total

def is_transactionsuccess(money_received, total_cost):
    if money_received >= total_cost:
        change=round(money_received - total_cost, 2)
        global profit
        profit+=total_cost

        print(f"Your change is ${change}.")
        return True
    
    else:
        print(f"Sorry thats not enough. Monedy refund")
        return False
    
def makecoffee(choice, order_ingredients):
    print(order_ingredients)
    for item in order_ingredients:
        resources[item] - order_ingredients[item]


coffee_machine=True

while coffee_machine:
    choice=input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == 'off':
        coffee_machine=False

    elif choice == 'report':
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")

    else:
        drink=MENU[choice]
        if(checkResources(drink["ingredients"])):
            payment=processcoin()
            if is_transactionsuccess(payment, drink["cost"]):
                makecoffee(choice, drink["ingredients"])

