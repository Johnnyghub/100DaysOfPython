import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

validInput = False
users_choice = 3
choices = [rock, paper, scissors]

while not validInput:
    try:
        users_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    except:
        print("Please enter an integer.\n")

    if users_choice == 0:
        print(f"You chose:\n{rock}\n")
        validInput = True
    elif users_choice == 1:
        print(f"You chose:\n{paper}\n")
        validInput = True
    elif users_choice == 2:
        print(f"You chose:\n{scissors}\n")
        validInput = True
    else:
        print("Please enter either 0, 1 or 2 only.\n")

computers_choice = random.randint(0, 2)

print(f"The computer chose:\n{choices[computers_choice]}\n")

if users_choice == 0 and computers_choice == 2:
    print("You win!")
elif computers_choice == 0 and users_choice == 2:
    print("You lose!")
elif users_choice > computers_choice:
    print("You win!")
elif computers_choice > users_choice:
    print("You lose!")
elif computers_choice == users_choice:
    print("It's a draw!")
