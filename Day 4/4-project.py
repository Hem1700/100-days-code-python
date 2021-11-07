rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
if user_choice == 0:
    print(rock)
elif user_choice == 1:
    print(paper)
elif user_choice == 2:
    print(scissors)
else:
    print("wrong choice")

computer_choice =   random.randint(0,2)
if computer_choice == 0:
    print(rock)
elif computer_choice == 1:
    print(paper)
else:
    print(scissors)


if computer_choice == 0 and user_choice == 2: 
    print("Computer Wins")
elif computer_choice == 1 and user_choice == 0:
    print("Computer Wins")
elif computer_choice == 2 and user_choice == 1:
    print("Computer Wins")
elif computer_choice == 0 and user_choice ==1:
    print("User Wins")
elif computer_choice == 1 and user_choice ==2:
    print("User Wins")
elif computer_choice == 2 and user_choice == 0:
    print("User Wins")
elif computer_choice == user_choice:
    print("It is a draw")

