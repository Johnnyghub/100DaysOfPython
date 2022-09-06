age = 0
validInput = False

while not validInput:
    try:
        age = int(input("What is your current age?\n"))

        if age < 0 or age > 91:
            print("Please enter an age between 0 and 90n\n")
        else:
            validInput = True
    except:
        print("Please input a valid value for age.\n")

print(f"If you were to live until 90 years old:\nYou have {(90 * 365) - (age * 365)} days left to "
      f"live.\nYou have {(90*52)-(age*52)} weeks left to live.\nYou have {(90*12)-(age*12)} months left to live.")
