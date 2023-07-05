class MoneyMachine:
    CURRENCY = '$'
    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01,
    }

    def __init__(self):
        self.income = 0
        self.money_received = 0


    def report(self):
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        print("Please inert coins")
        for coin in self.COIN_VALUES:
            self.money_received += int(input(f"How many {coin}?: ")) * self.COIN_VALUES[coin]
            return self.money_received

    def make_payment(self, cost):
        self.process_coins()
        if self.monea_received >= cost:
           change = round(self.money_received-cost, 2)
           print(f"Here is your change {self.CURRENCY}{change}")
           self.income+=cost
           self.money_received = 0
           return True
        else:
            print("Sorry that's not enough money, Please insert more")
            self.money_received=0
            return False