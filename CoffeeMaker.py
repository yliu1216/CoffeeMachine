from menuItem import MenuItem
from menu import Menu

class Coffeemaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }

    def report(self):
        print(f"Water:{self.resources['water']}ml")
        print(f"Milk:{self.resources['milk']}ml")
        print(f"Coffee-Beans:{self.resources['coffee']}g")

    def is_resource_sufficient(self, drink):
        can_make = True
        for item in drink.ingredients:
            if drink.ingredients[item] > self.resources[item]:
                print(f"Sorry, there is not enough {item}. ")
                can_make=False
        return can_make

    def make_coffee(self, order):
        if self.is_resource_sufficient():
            for item in order.ingredients:
               self.resources[item]-=order.ingredients[item]
            ''' water_left = self.resources['water']-order.ingredients['water']
            milk_left = self.resources['milk']-order.ingredients['milk']
            coffee_left = self.resources['coffee']-order.ingredients['coffee']'''
            print(f"{order.name} is on the way ☕️. Enjoy!, resource available:\n "
                  f"water:{self.resources['water']}ml\n"
                  f"Milk:{self.resources['milk']}ml\n"
                  f"coffee-beans:{self.resources['coffee']}g\n")

