print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
def game():
    print("Welcome to Treasure Island.")
    print("Your mission is to find the treasure.") 

    road = input("You are at a crossroad which way do you want to go? L for left and R for Right ")
    if road == "L":
        swim = input("There is a lake, do you want to swim or wait for a boat? S for Swim and W for Wait ")
        if swim == "S":
            door = input("There are two doors, which one do you prefer? R for Red door, B for Blue door, or Y for Yellow door ")
            if door == "Y":
                print("YOU WIN!")
            elif door == "R":
                print("You were burnt in fire. GAME OVER!")
            elif door == "B":
                print("You were eaten by beasts. GAME OVER!")  
            else:
                print("GAME OVER!") 
        else:
            print("You were attacked by trout. GAME OVER!")
    else:
        print("Your fell into a hole. GAME OVER!")


game()
    