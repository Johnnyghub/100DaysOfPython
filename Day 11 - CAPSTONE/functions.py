import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]  # 1 represents ace, last 3 10s represent J Q K


def deal_card(to_player):
    """Deals a random card to the player's deck passed as a parameter, also checks whether or not the value of
     an ace should be 1 or 11 automatically. Returns a string version of the card appended to add to display array."""

    card = random.choice(cards)

    if card == 1:
        if (sum(to_player) + 11) <= 21:  # if it does not bust the hand, counts as 11
            to_player.append(11)  # only the first ace counts as 11, otherwise guaranteed to bust

        else:
            to_player.append(card)  # subsequent aces count as

        return 'A'
    else:
        to_player.append(card)

        if card == 10:  # if 10, return randomly between 10, J, Q, and K
            return random.choice(['10', 'J', 'Q', 'K'])
        else:
            return str(card)


def find_winner(players_cards, dealers_cards, players_display, dealers_display):
    """Compares scores to find the winner of a game covering all possible score combinations. Display arrays needed
    to be passed considering python cannot concatenate arrays of ints."""

    if sum(players_cards) < 21:
        if sum(dealers_cards) > 21:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nPlayer wins! Dealer Busts!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        elif sum(dealers_cards) < sum(players_cards):
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nPlayer wins!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        elif sum(dealers_cards) > sum(players_cards):
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nDealer wins!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        elif sum(dealers_cards) == sum(players_cards):
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nIt's a draw!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        elif sum(dealers_cards) == 21:
            if len(dealers_cards) == 2:
                print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
                print("\nDealer wins! Dealer got a blackjack!\n")
                print("Revealing dealer's hand....")
                print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

            else:
                print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
                print("\nDealer wins! Dealer hit 21!\n")
                print("Revealing dealer's hand....")
                print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

    if sum(players_cards) > 21:
        if sum(dealers_cards) > 21:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nIt's a draw! Both players busted.\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        elif sum(dealers_cards) == 21:
            if len(dealers_cards) == 2:
                print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
                print("\nDealer wins! Dealer got a blackjack!\n")
                print("Revealing dealer's hand....")
                print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")
            else:
                print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
                print("\nDealer wins! Dealer hit 21!\n")
                print("Revealing dealer's hand....")
                print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        else:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nDealer wins! Player busted.\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

    if sum(players_cards) == 21 and len(players_cards) > 2:  #we already check if the player reaches an immediate 21
        if sum(dealers_cards) != 21:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nPlayer wins!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        elif sum(dealers_cards) == 21 and len(dealers_cards) == 2:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nDealer wins! Dealer got a blackjack whereas player hit 21 with more than 2 cards.\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")

        else:
            print(f"Player's cards: {' '.join(players_display)}. Total: {sum(players_cards)}.")
            print("\nDraw! Both players hit 21 exactly!\n")
            print("Revealing dealer's hand....")
            print(f"\nDealer's cards: {' '.join(dealers_display)}. Total: {sum(dealers_cards)}.")
