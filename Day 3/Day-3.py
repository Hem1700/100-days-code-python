# print("Welcome to the rollercoaster!")
# height = int(input("What is your height in cm? "))
# age = int(input("What is your age? "))
# bill = 0

# if height >= 120:
#     if age < 12:
#         bill = 3
#     elif age > 12 and age <18:
#         bill = 7
#     elif age >45 and age<55:
#         print("Your ride is free")
#     else:
#         bill = 12 
#     photo = input("Do you want a photograph? y or n ? ")
#     if photo == 'y':
#         bill += 3

#     print(f"Your total bill is {bill}")     
# else:
#     print("Can't ride")



# # Day-3-1 Exercise

# number = int(input("Enter a number to check whether it is odd or even "))
# if number % 2 ==0:
#     print("It is an even number")
# else:
#     print("It is an odd number")



# #Day-3-2 Exercise

# height = float(input("Enter your height in m: "))
# weight = float(input("Enter your weight in kg: "))

# bmi = round(weight /(height*height))

# if bmi < 18.5:
#     print(f"Your BMI is {bmi}, you are underweight")
# elif bmi>18.5 and bmi<25:
#     print(f"Your BMI is {bmi}, you have a normal weight")
# elif bmi>25 and bmi<30:
#     print(f"Your BMI is {bmi}, you are slightly overweight")
# elif bmi>30 and bmi<35:
#     print(f"Your BMI is {bmi}, you are obese")
# elif bmi>35:
#     print(f"Your BMI is {bmi}, you are clinically obese")



# # Day-3-3 Exercise

# year = int(input("Which year do you want to check? "))

# if year % 4 == 0:
#     if year % 100 ==0:
#         if year % 400 == 0:
#             print("It is a leap year")
#         else:
#             print("It is not a leap year")
#     else:
#         print("It is  a leap year") 
# else:
#     print("It is not a leap year")





# # Day-3-4- Exercise

# print("Welcome to Python Pizza Deliveries! ")
# size = input("What size pizza do you want?S, M, or L ")
# add_pepperoni = input("Do you want pepperoni? Y or N ")
# extra_cheese = input("Do you want extra cheese? Y or N ")
# total_bill = 0
# if size == "S":
#     total_bill = 15
#     if add_pepperoni == "Y":
#         total_bill += 2
#         if extra_cheese == "Y":
#             total_bill += 1    
#     elif add_pepperoni == "N":
#         total_bill = 15
#         if extra_cheese == "Y":
#             total_bill +=1

# elif size == "M":
#     total_bill = 20
#     if add_pepperoni == "Y":
#         total_bill += 3
#         if extra_cheese == "Y":
#             total_bill += 1    
#     elif add_pepperoni == "N":
#         total_bill = 20
#         if extra_cheese == "Y":
#             total_bill +=1

# elif size == "L":
#     total_bill = 25
#     if add_pepperoni == "Y":
#         total_bill += 3
#         if extra_cheese == "Y":
#             total_bill += 1    
#     elif add_pepperoni == "N":
#         total_bill = 25
#         if extra_cheese == "Y":
#             total_bill +=1


# print(f"Your final Bill is: {total_bill}")





# Day 3- 5 Exercise

print("Welcome to the Love Calculator!\n")
name1 = input("What is your name?\n").lower()
name2 = input("What is their name?\n").lower()
combined_name = name1 + name2 
true = 0
t= 0
r =0
u= 0
e = 0
love = 0
l =0
o = 0
v = 0
e = 0

t = combined_name.count('t')
r = combined_name.count('r')
u = combined_name.count('u')
e = combined_name.count('e')
true = t + r + u + e

l = combined_name.count('l')
o = combined_name.count('o')
v = combined_name.count('v')
e = combined_name.count('e')
love  = l + o + v + e

final_score = str(true) + str(love)
if int(final_score) <10 or int(final_score)> 90:
    print(f"Your score is {int(final_score)}, you go together like coke and mentos")
elif int(final_score) >40 and int(final_score)< 50:
    print(f"Your score is {int(final_score)}, you are alright together")
else:
    print(f"Your score is {final_score}")    
