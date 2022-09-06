cont = True
another_calc = 'yes'


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def input_num(first_or_next):  # first_or_next represents the word printed in the string
    num = 0
    validInputs = False

    while not validInputs:
        try:
            num = float(input(f"\nEnter the {first_or_next} number: "))
            validInputs = True  # If no errors caught, escape the while loop
        except:
            print("Please enter a valid input for your number.\n")

    return num


num1 = input_num("first")

while cont:
    num2 = input_num("next")

    print("\nPossible Operations:")
    for symbol in operations:
        print(symbol)

    validOperation = False
    operation = ''
    answer = 0  # placeholders to avoid yellow lines in code

    while not validOperation:
        try:
            operation = input("\nPlease enter the operation you want to carry out: ")
            answer = operations[operation](num1, num2)
            validOperation = True
        except:
            print("\nPlease enter a valid operation.\n")

    print(f"\n{num1} {operation} {num2} = {answer}\n")

    another_calc = input(f"Would you like to use {answer} in a new calculation? 'Yes' will carry it forward, 'New' will"
                         f" start a brand new calculation, and any other input will end the program: ").lower()

    if another_calc == 'yes':
        cont = True
        num1 = answer
    elif another_calc == 'new':
        cont = True
        input_num("first")
    else:
        cont = False
        print("\nThanks for using the calculator program!")

