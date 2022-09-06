import random
from data import data


def get_random_entry():
    """Returns a random entry's formatted data as a new dict entry. Follower count labelled 'follower_count' and
    output data labelled 'output_statement'."""

    entry = random.choice(data)

    return_data = {'follower_count': entry['follower_count'],
                   'output_statement': f"{entry['name']}, a {entry['description']}, from {entry['country']}."}

    return return_data  # we could return the dict directly, but to simplify the main program it is easier to return this


def compare_followers(users_choice, other_option):
    """Compares the users choice with the other option and returns True if user's choice is greater"""
    if users_choice > other_option:
        return True
    elif users_choice < other_option:
        return False
    else:
        return True  # if equal, return true in order to not penalize user


def input_choice():
    """Returns a user's choice or A or B with validation."""
    choice = ''

    while choice == '':
        choice = input("Who has more followers? Type A or B: ").upper()

        if choice != 'A' and choice != 'B':
            print("\nPlease enter only 'A' or 'B'.\n")
            choice = ''

    return choice
