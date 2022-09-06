from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine_on = True
menu = "What would you like?" \
       "\n1. ☕ Espresso" \
       "\n2. ☕ Latte" \
       "\n3. ☕ Cappuccino" \
       "\n4. 📝 Generate Report" \
       "\n9. ⛔ Exit" \
       "\nEnter your choice: "

coffee_machine = CoffeeMaker()
money_machine = MoneyMachine()
drinks_menu = Menu()


def make_coffee(drink):
    if coffee_machine.is_resource_sufficient(drink):
        if money_machine.make_payment(drink.cost):
            coffee_machine.make_coffee(drink)


while machine_on:
    choice = input(menu)
    print()

    if choice == '1':
        make_coffee(drinks_menu.find_drink('espresso'))
    elif choice == '2':
        make_coffee(drinks_menu.find_drink('latte'))
    elif choice == '3':
        make_coffee(drinks_menu.find_drink('cappuccino'))
    elif choice == '4':
        coffee_machine.report()
        money_machine.report()
    elif choice == '9':
        print("Thank you for using this coffee machine!\n")
        machine_on = False
    else:
        print("Please enter a valid choice.\n")
