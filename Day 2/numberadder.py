validinput = False
first_digit = 0
second_digit = 0

while not validinput:
    try:
        two_digit_number = input('Enter a two digit number please:\n')
        if len(two_digit_number) == 2:
            first_digit = int(two_digit_number[0])
            second_digit = int(two_digit_number[1])
            validinput = True
        else:
            print("Please enter a valid two digit number\n")
            validInput = False
    except:
        validinput = False
        print("Please enter a valid two digit number\n")

print("The result of adding the two numbers together is " + str(first_digit + second_digit) + ".")
