def enter_money():
    """Asks how many coins of each kind user enters, calculates total balance and returns it."""
    validInputs = False
    quarters = 0
    dimes = 0
    pennies = 0
    nickels = 0  # to remove annoying yellow lines, placeholders

    while not validInputs:
        try:
            quarters = int(input("Insert number of quarters: "))
            dimes = int(input("Insert number of dimes: "))
            nickels = int(input("Insert number of nickels: "))
            pennies = int(input("Insert number of pennies: "))
            validInputs = True  # if no inputerrors detected
        except:
            print("\nPlease enter integers only.\n")

    return (quarters * 0.25) + (dimes * 0.1) + (nickels * 0.05) + (pennies * 0.01)  # returns balance


def check_resources(resources_available, resources_required, type_of_coffee):
    """Checks if there are enough resources and returns true or false"""

    enough_resources = True

    if resources_available['water'] < resources_required[type_of_coffee.lower()]['ingredients']['water']:
        print("There is not enough water in the machine.\n")
        enough_resources = False
    if resources_available['coffee'] < resources_required[type_of_coffee.lower()]['ingredients']['coffee']:  # not elif because both can be possible
        print("There is not enough coffee in the machine.\n")
        enough_resources = False
    if resources_available['milk'] < resources_required[type_of_coffee.lower()]['ingredients']['milk']:  # not elif because both can be possible
        print("There is not enough milk in the machine.\n")
        enough_resources = False

    return enough_resources


def make_coffee(resources_available, resources_required, type_of_coffee):
    """Checks if there are enough resources (passed as parameters), prompts user to enter coins and then gives them
    coffee if all checks passed, removes resources used and adds profit"""

    enough_resources = check_resources(resources_available, resources_required, type_of_coffee)

    if enough_resources:
        print(f"Please enter ${round(resources_required[type_of_coffee.lower()]['cost'], 2)}.\n")
        balance = enter_money()

        if balance >= resources_required[type_of_coffee.lower()]['cost']:
            change = balance - resources_required[type_of_coffee.lower()]['cost']

            resources_available['money'] += resources_required[type_of_coffee.lower()]['cost']  # add cost to machine profits
            resources_available['water'] -= resources_required[type_of_coffee.lower()]['ingredients']['water']  # remove other resources
            resources_available['coffee'] -= resources_required[type_of_coffee.lower()]['ingredients']['coffee']
            resources_available['milk'] -= resources_required[type_of_coffee.lower()]['ingredients']['milk']

            if change > 0:
                print(f"\nYour change is ${round(change, 2)}. Enjoy your {type_of_coffee.lower()}!\n")
            else:
                print(f"\nEnjoy your {type_of_coffee.lower()}!\n")
        else:
            print(f"Sorry, you did not enter enough money. You entered ${round(balance, 2)}, you need ${round(resources_required[type_of_coffee.lower()]['cost'], 2)}.\n")


def process_report(resources_available):
    print(f"Water: {resources_available['water']}ml")
    print(f"Milk: {resources_available['milk']}ml")
    print(f"Coffee: {resources_available['coffee']}g")
    print(f"Money: ${round(resources_available['money'], 2)}\n")
