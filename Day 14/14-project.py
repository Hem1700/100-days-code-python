from art import logo, vs
from game_data import data
import random


def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']
    return f"{name}, a {description}, from {country}"


def selection():
    return random.choice(data)


def compare_choice(guess, choice_1, choice_2):
    if choice_1 > choice_2:
        return guess == 'a'
    else:
        return guess =='b'    
        


def game():
    print(logo)
    score = 0
    should_continue = True
    account_a = selection()
    account_b = selection()

    while should_continue:
        account_a = account_b
        account_b = selection()

        while account_a == account_b:
            account_b = selection()

        print(f"Compare A: {format_data(account=account_a)} ")
        print(vs)
        print(f"Against B: {format_data(account=account_b)}")    

        guess = input("Who has more followrs? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = compare_choice(guess, a_follower_count, b_follower_count)

        if is_correct:
            score +=1
            print(f"You're right! Current Score: {score}")
        else:
            should_continue = False
            print(f"Sorry that's wrong. Final Score: {score}")    





game()