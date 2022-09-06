year = 0
validInput = False

while not validInput:
    try:
        year = int(input("Which year would you like to check? "))
        validInput = True
    except:
        print("Please enter a valid year")

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print(f"{year} is a leap year.")
        else:
            print(f"{year} is not a leap year.")
    else:
        print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
