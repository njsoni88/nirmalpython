
from Coffee_Machine_dict import *

profit = 0
def change_calculation(total, price):
    if price < total:
        change = total - price
        return f"Your change is {change}"
    else:
        return "Sorry that's not enough money. Money refunded."


price = 0

is_on = True
while is_on:
    customer_choice = input("What would you like to have? Type Espresso, Latte, Cuppucino: ").lower()
    if customer_choice == 'off':
        is_on = False
    elif customer_choice == "report":
        print(f"water: {resources['water']}ml")
        print(f"milk: {resources['milk']}ml")
        print(f"coffee: {resources['coffee']}g")
        print(f"money: ${profit}")
    else:
        drink = MENU[customer_choice]
        print(drink)


# if customer_choice == 'espresso':
#     price = MENU[1]
#     print(f"esps {price}")
# elif customer_choice == 'b':
#     price = 2.5
# else:
#     price = 3.0

print("Please insert coins.")
quarter = round(0.25 * int(input("How many quarters?: ")), 2)
dime = round(0.10 * int(input("How many dimes?: ")), 2)
nickel = round(0.05 * int(input("How many nickels?: ")), 2)
penny = round(0.01 * int(input("How many pennies?: ")), 2)

print(f"quarter {quarter}, dime {dime}, nickel {nickel}, penny {penny}")

total = round((quarter + dime + nickel + penny), 2)
print(total)

print(change_calculation(total, price))

# TODO: total up the money
#  TODO: give change.
