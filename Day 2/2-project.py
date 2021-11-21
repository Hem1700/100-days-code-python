import os


def tip_calulator():
    go_again = True
    print("Welcome to the tip calculator!\n")
    while go_again:
        bill = float(input("What was the total bill? $"))
        tip_percent = float(input("How much tip would you like to give? 10, 12, or 15? "))
        total_people = int(input("How many people to split the bill? "))
        total_bill=  float((tip_percent * bill)/100 + bill)
        total_contribution = round(total_bill/total_people, 2)
        print(f"Each person should pay: ${total_contribution}")
        answer = input("Want to calulate again? Type 'y' or 'n': ")
        if answer == 'y':
            go_again = True
            os.system('cls')
        else:
            go_again = False    


tip_calulator()