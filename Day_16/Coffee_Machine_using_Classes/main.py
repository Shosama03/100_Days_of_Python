from menu import Menu,MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

should_continue=True
menu= Menu()
coffee_maker=CoffeeMaker()
money_machine=MoneyMachine()


while should_continue:
    user_input=input(f"What would you like ({menu.get_items()}): ").strip().lower()
    if user_input == 'off':
        should_continue=False
    elif user_input == 'report':
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(user_input)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)
            
                