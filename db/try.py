class Drinks:
    def __init__(self, name, amount, quantity):
        self.name = name
        self.amount = amount
        self.quantity = quantity

    def ads(self):
        print(f'We sell {self.name} here!')

obj1 = Drinks('latte',23,5)
obj1.ads()