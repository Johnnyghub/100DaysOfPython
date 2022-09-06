print("Welcome to the love calculator.\n")

name1 = (input("What is your name?\n")).lower()
name2 = (input("What is their name?\n")).lower()

combinedname = name1 + name2

first_number = str(combinedname.count("t") + combinedname.count("r") + combinedname.count("u") + combinedname.count("e"))
second_number = str(combinedname.count("l") + combinedname.count("o") + combinedname.count("v") + combinedname.count("e"))
compatibility = int(first_number + second_number)  # Need to change back to int to compare in if statement

if compatibility < 10 or compatibility > 90:
    print(f"Your love compatibility is {compatibility}%. You go together like coke and mentos.")
elif 40 <= compatibility <= 50:
    print(f"Your love compatibility is {compatibility}%. You go alright together")
else:
    print(f"Your love compatibility is {compatibility}%.")
