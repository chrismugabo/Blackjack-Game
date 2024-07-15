import random
from art import logo
import os

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Calculate the score of a hand of cards."""
    total = sum(cards)
    if 11 in cards and 10 in cards and len(cards) == 2:
        return 0  # Blackjack
    if 11 in cards and total > 21:
        cards.remove(11)
        cards.append(1)
    return total

def compare(user_score, computer_score):
    """Compare user's score to computer's score and return the result."""
    if user_score == computer_score:
        return "It's a draw!"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack!"
    elif user_score == 0:
        return "Win with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    end_of_game = False
    while not end_of_game:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            end_of_game = True
        else:
            choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if choice == "y":
                user_cards.append(deal_card())
            else:
                end_of_game = True

    while computer_score < 17 and computer_score != 0:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

# Main loop to keep the game running
while True:
    os.system('clear')  # Corrected to use os.system('clear') for consistency
    play_game()
    choice = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ")
    if choice.lower() != "y":
        break
    


    