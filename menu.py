from menuItem import MenuItem
class Menu:
    def __init__(self):
        self.menu = [
            MenuItem(name="espresso", water=50, coffeebeans=18, cost=1.5, milk=0),
            MenuItem(name="latte", water=200, milk=150, coffeebeans=24, cost=2.5 ),
            MenuItem(name="cappuccino", water=250, milk=100, coffeebeans=24, cost=3)
        ]

    def get_items(self):
        options = ""
        for item in self.menu:
            options+=f"{item.name}/"
        return options

    def find_drink(self, ordername):
        for item in self.menu:
            if item.name==ordername:
                return item
            else:
                print("item does not exist or it is not available. ")

