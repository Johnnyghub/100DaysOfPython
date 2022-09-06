weight = 0
height = 0
validInput = False

while not validInput:
    try:
        weight = float(input("Please enter your weight in kg:\n"))
        height = float(input("Please enter your height in cm:\n"))

        if weight < 20 or weight > 200:
            print("Please enter a valid weight between 20 and 200 kg.\n")
            validInput = False
        elif height < 90 or height > 250:
            print("Please enter a valid height between 90 and 250 cm\n")
            validInput = False
        else:
            validInput = True  # If the values are valid, break out of the while loop
    except:
        print("Please enter a valid height and/or weight\n")
        validInput = False

print(f"Your BMI is {round(weight / ((height/100) ** 2), 2)}.")  # BMI calculation done inline + example of fstring
