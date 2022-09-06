import os
from art import logo
from functions import deal_card
from functions import find_winner

play = True  # continue playing the game

while play:
    print(f"{logo}\n")  # variables initialized and logo printed in loop because they need to be reset every turn

    players_turn = True  # player gets to choose hit or stand

    dealers_cards = []
    players_cards = []

    dealers_display = []
    players_display = []  # they are arrays of ints, so we need to switch to ints to use .join

    dealers_display.append(deal_card(to_player=dealers_cards))
    dealers_display.append(deal_card(to_player=dealers_cards))

    if sum(dealers_cards) < 17:
        dealers_display.append(deal_card(to_player=dealers_cards))  # if dealer is under 17, forced to hit, else stand

    print(f"Dealer's first card: {dealers_display[0]}. (Value: {dealers_cards[0]})\n")

    players_display.append(deal_card(to_player=players_cards))
    players_display.append(deal_card(to_player=players_cards))

    if sum(players_cards) == 21:
        if sum(dealers_cards) != 21:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nPlayer wins! Blackjack!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")
            players_turn = False
        else:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nDraw! Both players achieved a blackjack!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")
            players_turn = False

    while players_turn:
        hit_or_stand = ''
        print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")

        while hit_or_stand == '':
            hit_or_stand = input("\nEnter 'hit' to recieve another card, or 'stand' to end your turn: ").lower()
            print()

            if hit_or_stand != 'hit' and hit_or_stand != 'stand':
                print("Please enter a valid input.")
                hit_or_stand = ''

        if hit_or_stand == 'hit':
            players_display.append(deal_card(to_player=players_cards))

            if sum(players_cards) >= 21:
                players_turn = False  # if bust/blackjack end turn by force

        if hit_or_stand == 'stand':
            players_turn = False

    find_winner(players_cards, dealers_cards, players_display, dealers_display)

    if input("\nType 'y' for a rematch, anything else to exit: ").lower() == 'y':
        os.system('cls')  # clear screen (only works outside IDEs, no alternative)
    else:
        play = False

print("\nThank you for playing python blackjack!")
