import random

intnumber = random.randint(100, 200)
print(intnumber)

floatnumber = random.uniform(1, 5)
floatnumber1 = random.random() * 5
print(floatnumber)
print(floatnumber1)


# Day 4-1 Exercise

toss_number = random.randint(0, 1)
if toss_number == 0:
    print("Tails")
else:
    print("Heads")

 # Lists

states = ["Gujarat", "Maharashtra", "Punjab", "Kerela", "Goa"]
states[1] = "Bengal"
states.append("Maharashtra")

# dirty_dozens = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples",
#                 "Grapes", "Peaches", "Cherrie", "Pears", "Tomatoes", "Celery", "Potatoes"]

fruits = ["Strawberries","Nectarines", "Apples","Grapes", "Peaches", "Cherrie", "Pears",]
vegetables = [ "Spinach", "Kale","Tomatoes", "Celery", "Potatoes"]
dirty_dozen = [fruits, vegetables]
print(dirty_dozen)

# Day-4-2 Exercise


names_string = input("Give me everybody's names, separated by a comma.")
names = names_string.split(",")
random_selector = random.randrange(0, len(names)-1)
print(f"{names[random_selector]} is going to buy the meal today!")


# Day-4-3 Exercise

row1 = ["⬜️", "⬜️", "⬜️"]
row2 = ["⬜️", "⬜️", "⬜️"]
row3 = ["⬜️", "⬜️", "⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
first_position = int(position[0])
second_position = int(position[1])
map[second_position-1][first_position-1] = "X"
print(f"{row1}\n{row2}\n{row3}")
