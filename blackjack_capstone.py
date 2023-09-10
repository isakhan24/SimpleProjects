#Blackjack Capstone Project
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def blackjack():
    user_cards = []
    dealer_cards = []

    for num in range (0, 2):
        user_cards.append(deal_card())
        dealer_cards.append(deal_card())
    user_total =  sum(user_cards)

    print(f"User cards: {user_cards}\nDealer first card: {dealer_cards[0]}\nCurrent Score: {user_total}")
    prompt_card = True

    while prompt_card:
        user_another: str = input("Would you like another card? (y/n)\n").lower()
        if user_another == "y":
            user_cards.append(deal_card())
            user_total: int = sum(user_cards)

            if 11 in user_cards and user_total > 21:
                user_cards: list = [1 if item == 11 else item for item in user_cards]
                user_total: int = sum(user_cards)
            print(f"User cards: {user_cards}\nDealer first card: {dealer_cards[0]}\nCurrent Score: {user_total}")
            if user_total > 21:
                prompt_card = False
        else:
            prompt_card = False
            print(f"User cards: {user_cards}\nCurrent Score: {user_total}")
    dealer_total: int = sum(dealer_cards)

    dealer_another = False
    if dealer_total < user_total and dealer_total < 21:
        dealer_another = True
    while dealer_another:
        dealer_cards.append(deal_card())
        dealer_total: int = sum(dealer_cards)

        if 11 in dealer_cards and dealer_total > 21:
            dealer_cards: list = [1 if item == 11 else item for item in dealer_cards]
            dealer_total: int = sum(dealer_cards)

        if dealer_total < user_total and dealer_total < 21:
            dealer_another = True
        else:
            dealer_another = False

    print(f"Dealer cards: {dealer_cards}\nDealer Score: {dealer_total}")

    winner(user_total, dealer_total)
    play_again()

def winner (user, dealer):
    if user == dealer:
        print(f"Tie with user and dealer scores of {user}")
    else:
        if user == 21 or dealer > 21 and user < 21:
            print(f"User wins with a score of {user}")
        elif dealer == 21 or user > 21:
            print(f"Dealer wins with a score of {dealer}")
        elif dealer and user < 21:
            if dealer > user:
                print(f"Dealer wins with a score of {dealer}")
            else:
                print(f"User wins with a score of {user}")
        else:
            return

def play_again():
    user_input = input("Would you like to play again? (y/n) ").lower()

    if user_input == 'y':
        print("\n\n\n\n\n\n\n")
        blackjack()
    else:
        print("Thank you for playing Blackjack.")


def main():
    print("Welcome to Blackjack")
    start = input("Would you like to play a game? (y/n) ").lower()

    if start == 'y':
        blackjack()
    else:
        print("Thank you for playing Blackjack.")

main()
