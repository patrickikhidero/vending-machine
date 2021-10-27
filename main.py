# Entry point of the application by running the Menu
# import the following 1. coffee_maker 2. payment 3. menu
# Prompt user by asking “​What would you like? (espresso/latte/cappuccino):”​
## - Check the user’s input to decide what to do next 
## - Turn off the Coffee Machine by entering “​off”​to the prompt.
## - When the user enters “report” to the prompt,
##  a report should be generated that shows the current resource values.

from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from payment import MachinePayment

will_continue = True
menu = Menu()
name = menu.get_items()
money_machine = MachinePayment()
coffee_maker = CoffeeMaker()
while will_continue:
    choice = input(f"What would you like? ({name}): ").lower()
    if choice == "off":
        will_continue = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)