bill = 0

print("Welcome to the pizza delivery service.\n")
size = (input("What size pizza would you like? (S, M or L): ")).lower()  # To make inputs un-case sensitive
add_pepperoni = (input("Would you like to add pepperoni to your pizza? (Y / N): ")).lower()  #Since no validation
extra_cheese = (input("Do you want extra cheese on your pizza? (Y / N): ")).lower()

if size == 's':
    bill += 15
    if add_pepperoni == 'y':
        bill += 2
elif size == 'm':
    bill += 20
    if add_pepperoni == 'y':
        bill += 3
elif size == 'l':
    bill += 25
    if add_pepperoni == 'y':
        bill += 3
else:
    print("Invalid size")

if extra_cheese == 'y':
    bill += 1

# It is possible that the first if statement does not get run due to invalid input, so this check is to prevent
# Bad print statemnets

if bill >= 15:  # Minimum bill value, since cheapest pizza is 15
    print(f"Your final bill is ${bill}.")
