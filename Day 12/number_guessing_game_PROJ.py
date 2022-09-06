import random

cpu_num = random.randint(1,100)

print("Welcome to the number guessing game!\n")

print("I'm thinking of a number between 1 and 100.\n")


def select_difficulty():
    difficulty = ''
    while difficulty == '':
        difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        print()

        if difficulty == 'easy':
            return 10  # attempts
        elif difficulty == 'hard':
            return 5  # attempts
        else:
            difficulty = ''  # don't exit the loop
            print("\nPlease enter a valid difficulty.\n")


attempts = select_difficulty()

while attempts > 0:
    print(f"You have {attempts} attempts remaining. Make a guess!")
    try:
        guess = int(input("\nPlease enter a guess: "))
    except:
        guess = ''
        print("\nPlease enter a valid guess.\n")

    if guess != '':
        if guess > cpu_num:
            print("\nYour number is greater than the number I'm thinking of.\n")

        if guess < cpu_num:
            print("\nYour number is smaller than the number I'm thinking of.\n")

        if guess == cpu_num:
            print("You guessed my number! Congrats!")
            attempts = 0  # You win, exit loop, will be -1

        attempts -= 1

if attempts == 0:  # lose condition
    print(f"You did not guess the number! The number was {cpu_num}!")
