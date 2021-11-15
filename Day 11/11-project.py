from art import logo
import random
import os

############### Our Blackjack House Rules #####################
## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.


def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_scores(card_list):
    if sum(card_list) == 21 and len(card_list) == 2:
        return 0
    if 11 in card_list and sum(card_list) > 21:
        card_list.remove(11)
        card_list.append(1)
    return sum(card_list)


def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_over = False

    for i in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while game_over != True:
        user_sum = calculate_scores(user_cards)
        computer_sum = calculate_scores(computer_cards)
        print(f"Your cards: {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_cards[0]}")
        if user_sum == 0 or computer_sum == 0 or user_sum > 21:
            game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True

    while computer_sum != 0 and computer_sum < 17:
        computer_cards.append(deal_card())
        computer_sum = calculate_scores(computer_cards)



    def compare(user_score, computer_score):
        if user_score == computer_score:
            print("It's a draw")
        elif computer_score == 0:
            print("Computer wins")
        elif user_score == 0:
            print("User wins")
        elif user_score > 21:
            print("Computer Wins")
        elif computer_score > 21:
            print("User wins") 
        elif computer_score > user_score:
            print("Computer wins")
        elif user_score > computer_score:
            print("User Wins")               


    print(f"Your final hand: {user_cards} and final score: {user_sum}")
    print(f"Computer's final hand: {computer_cards} and computer's score: {computer_sum}")
    compare(user_score= user_sum , computer_score= computer_sum)



while input("Do you want to play a game of BlackJack? Type 'y' or 'n':  ") == 'y':
    os.system('cls')
    play_game()