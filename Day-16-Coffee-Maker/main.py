from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on:
    choice = input(f'What do you want to order ({menu.get_items()}) : ')
    if choice == 'report':
        coffee_maker.report()
        money_machine.report()
    elif choice == 'off':
        is_on = False
    else:
        order = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(order):
            if money_machine.make_payment(order.cost):
                coffee_maker.make_coffee(order)
