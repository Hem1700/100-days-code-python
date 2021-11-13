import art
import os


print(art.logo)
print("Welcome to the secret auction program\n")
bidding_dict = {}
continue_playing = 'yes'
winner = 0
winner_name = ''
while continue_playing != 'no':
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    bidding_dict[name] = bid
    for bidder in bidding_dict:
        if winner <= bidding_dict[bidder]:
            winner = bidding_dict[bidder]
            winner_name = bidder
    continue_playing = input(
        "Are there any other bidders? Type 'yes' or 'no' ")     
    if continue_playing == "no":      
        print(f"The winner is {winner_name} with a bidding of ${winner}")
    if continue_playing == "yes":
        os.system('cls')
