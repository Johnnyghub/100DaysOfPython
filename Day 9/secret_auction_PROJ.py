import os

logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
print("\nWelcome to the secret auction program.")

bidders = {}
cont = 'yes'
name = ''
bid = -1

while cont == 'yes':
    name = input("\nWhat is your name? ")

    while bid == -1:
        try:
            bid = float(input("\nWhat is your bid? $"))

            if bid <= 0:
                bid = -1  # reset the bid to stay in the while loop
                print("\nPlease enter a bid greater than 0.")
        except:
            print("\nPlease enter a number for your bid. No other input will be accepted.")
            bid = -1

    bidders[name] = bid  # add the bid to the dict

    bid = -1  # reset bid so it re-enters the while loop

    cont = input("\nIs there another bidder? Anything other than 'yes' will end the program: ").lower()
    os.system('cls')  # Clear the screen everytime a new bid needs to be entered, or once the program ends

highest_bidder = max(bidders, key=bidders.get)  # retrieves the highest bidder from the dictionary
print(f"The highest bidder is {highest_bidder}, they won with a bid of ${round(bidders[highest_bidder], 2)}!")


