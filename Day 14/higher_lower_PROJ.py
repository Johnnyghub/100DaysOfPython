from art import logo, vs
from functions import get_random_entry, compare_followers, input_choice
from os import system

play = True
score = 0
first_turn = True
A = 0  # used to avoid annoying yellow lines

while play:
    print(f"{logo}\n")

    if first_turn:
        A = get_random_entry()
        print(f"Compare A: {A['output_statement']}")
        first_turn = False
    else:
        print(f"You're right! Your score is {score}!\n")  # since it only continues if user is correct, we only need this
        print(f"Compare A: {A['output_statement']}")

    print(f"{vs}\n")

    B = get_random_entry()  # B should always be regenerated

    while A == B:
        B = get_random_entry()  # B and A must never be equal, so loop until B is different just in case

    print(f"Against B: {B['output_statement']}\n")

    choice = input_choice()

    if choice == 'A':
        correct = compare_followers(A['follower_count'], B['follower_count'])
    else:
        correct = compare_followers(B['follower_count'], A['follower_count'])

    if correct:
        score += 1
        A = B  # move value of B to A to emulate higherlower.com
        # B will always be regenerated

        system('cls')  # clear screen
    else:  # if wrong, end the program
        play = False
        system('cls')

print(f"{logo}\n")
print(f"Sorry, that was wrong! Your score is {score}!\nThanks for playing higher lower!\n")
input()  # used to not immediately crash cmd after the program is done until the user clicks enter
