import random

print(random.randint(0, 2))

names_string = input("Enter everybody's names, seperated by a comma with no space afterwards: ")
bankers = names_string.split(",")

print(f"The banker that will pay the bill is {bankers[random.randint(0, (len(bankers)-1))]}.")

