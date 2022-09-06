import databank
import random
import os

guess = ""
chosen_word = random.choice(databank.wordbank)
display = ["_"] * len(chosen_word)  # create an empty display of length chosen_word where the default value is _
lives = 6
previous_guesses = []


def enter_guess():
    global guess
    while guess == "":
        guess = (input("\nPlease enter a character: ")).lower()

        if len(guess) != 1:
            print("\nPlease enter only 1 character.")
            guess = ""
        else:  # to avoid several possibly incorrect error messages at once
            if guess not in databank.letters:  # check if the input is a valid character, by comparing it to a letter array
                print("\nPlease enter a valid character, no integers or symbols.")
                guess = ""
            else:  # once again, to avoid multiple errors, only check if the previous two errors are not caught
                if guess in previous_guesses:
                    print("\nYou cannot guess the same letter twice.")
                    guess = ""


def check_letter():
    global guess, display, lives
    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if guess == chosen_word[i]:
                display[i] = guess
    else:
        lives -= 1

        if lives == 0:
            display = chosen_word

    print("\nWord: " + ' '.join(display))

    print(f"\nLetters guessed: {', '.join(previous_guesses)}")

    guess = ""  # reset guess for next round


def game():
    print(f"{databank.logo}\n\nWord: {' '.join(display)}")

    while "_" in display:
        print(f"\n{databank.stages[lives]}")
        enter_guess()
        os.system('cls')  # Clear the screen everytime a new guess is entered
        previous_guesses.append(guess)  # Prevents the user from guessing the same letter twice, correct or not
        check_letter()

    if lives > 0:
        print("\nYou Won!")
    else:
        print("\nYou Lost.")


game()
