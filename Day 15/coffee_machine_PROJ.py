import functions

machine_on = True
menu = "What would you like?" \
       "\n1. ☕ Espresso" \
       "\n2. ☕ Latte" \
       "\n3. ☕ Cappuccino" \
       "\n4. 📝 Generate Report" \
       "\n9. ⛔ Exit" \
       "\nEnter your choice: "

required_resources = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources_available = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

while machine_on:
    choice = input(menu)
    print()

    if choice == '1':
        functions.make_coffee(resources_available, required_resources, "espresso")
    elif choice == '2':
        functions.make_coffee(resources_available, required_resources, "latte")
    elif choice == '3':
        functions.make_coffee(resources_available, required_resources, "cappuccino")
    elif choice == '4':
        functions.process_report(resources_available)
    elif choice == '9':
        print("Thank you for using this coffee machine!\n")
        machine_on = False
    else:
        print("Please enter a valid choice.\n")
