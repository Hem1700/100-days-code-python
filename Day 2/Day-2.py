#Data Types
print("Hello"[0])
# Integer
print(123+ 345)
#123_234_325(123,234,325)
#Float
print(3.14159 +12.00)
#Boolean
True
False
# Type Conversion

# num_char = len(input("What is your name?\n"))
# print("Your name has " + str(num_char) +" " + "characters" )
# print(type(num_char))
# print(len(str(1234)))



# Day-2-1 - Exercise

num = input("Enter a two digit number\n")
sum = int(num[0]) + int(num[1])
print(sum)


# **  - exponent 
print(3**3)
# PEMDAS  - (), ** , * / , + -


# Day 2-2 - Exercise

height = float(input("Enter your height in m: "))
weight = float(input("Enter your weight in Kg: "))

bmi = weight / (height*height)
print(int(bmi))



print(round(8/3, 2))

print(8//3)    # To get answer in integer

#f strings
score = 0
heigh = 1.8
isWinning = True

print(f"your score is {score}, your height is {heigh} and your winning is {isWinning}") 



# Day 2-3 Exercise

age = input("What is your current age?\n")

years_left = 90 - int(age)
print(years_left)
month_left = years_left *12
week_left = years_left * 52
days_left = years_left * 365

print(f"You have {days_left} days, {week_left} weeks, and {month_left} months left.")