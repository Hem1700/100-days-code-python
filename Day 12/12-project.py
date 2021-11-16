from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()


def guess_number():
    randNum = random.randrange(1,100)  
    def easy_level():
        guess = int(input("Try to guess the number:"))
        lives = 10
        while lives != 0:
            if (guess == randNum):
                print (f"You got it! The number was {guess}")
                break
            if (guess > randNum):
                lives -= 1
                print ("Too High.")
                print(f"You have {lives} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))  
            if (guess < randNum):
                lives -=1
                print ("Too Low.")
                if lives ==0:
                    print("You've have run out of guesses, you lose")    
                    break
                print(f"You have {lives} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))            
    def hard_level(): 
        guess = int(input("Try to guess the number:"))
        lives = 5
        while lives != 0:
            if (guess == randNum):
                print (f"You got it! The number was {guess}")
                break
            if (guess > randNum):
                lives -= 1
                print ("Too High.")
                print(f"You have {lives} attempts remaining to guess the number.")
                guess = int(input("Make a guess: "))  
            if (guess < randNum):
                lives -=1
                print ("Too Low.")
                if lives ==0:
                    print("You've have run out of guesses, you lose")    
                    break
                print(f"You have {lives} attempts remaining to guess the number.")
            
                guess = int(input("Make a guess: "))  
  
    if difficulty == 'easy':
        easy_level()
    elif difficulty == 'hard':
        hard_level()

guess_number()