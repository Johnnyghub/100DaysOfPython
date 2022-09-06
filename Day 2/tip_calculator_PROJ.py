total_bill = 0
tip_percent = 0
people_splitting_bill = 0
validInput = 0

while not validInput:
    try:
        total_bill = float(input("What was the total bill? $"))
        tip_percent = float(input("What percentage tip would you like to give? "))
        people_splitting_bill = int(input("How many people are splitting the bill? "))

        if total_bill <= 0:
            print("Bill cannot be 0$ or less.\n")
        elif tip_percent < 0:
            print("Tip cannot be less than 0%.\n")
        elif people_splitting_bill < 1:
            print("At least 1 person has to be paying for the bill.\n")
        else:
            validInput = True
    except:
        print("Please enter a valid number for bill/tip/number of people.\n")

final_bill = round((total_bill * ((tip_percent + 100) / 100)), 2)
each_person_pays = round((final_bill / people_splitting_bill), 2)

print(f"\nThe final bill is ${final_bill}, which means each person should pay ${each_person_pays}.")
