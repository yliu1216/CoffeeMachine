'''
1. coffee menu
2. resources
3. money exchange system
4. check transaction

'''
from menu import Menu
from menuItem import MenuItem
from CoffeeMaker import Coffeemaker
from MoneyMachine import MoneyMachine

CM = Coffeemaker()
MM = MoneyMachine()
menu = Menu()

is_on = True
while is_on:
    options = menu.get_items()
    choice = input(f"what is your coffee selection, {options}? ").lower()
    if choice == "off":
        is_on = False
    elif choice == "report":
        CM.report()
        MM.report()
    else:
        drink = menu.find_drink(choice)

        if CM.is_resource_sufficient(drink) and MM.make_payment(drink.cost):
            CM.make_coffee(drink)
