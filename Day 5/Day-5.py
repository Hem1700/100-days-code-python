# loops
fruits = ['apple', 'peach', 'pear']
for fruit in fruits:
    print(fruit)
    print(fruit + " " + "Pie")
sum = 0
for n in range(1,101):
    sum +=n
print(sum)


# Day-5-1 Exercise

student_heights = input("Input a list of student heights").split()
sum = 0
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
    sum = sum+student_heights[n]

average = sum/len(student_heights)
print(average)


# Day-5-2 Exercise

student_scores = input("Input a list of student scores").split()
highest_score = 0
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n]) 
    print(student_scores[n])
    if student_scores[n] > highest_score:
        highest_score = student_scores[n]
print(f"The highest score in the class is: {highest_score}")



# Day-5-3 Exercise

even_sum = 0
for n in range(0,101,2):
    even_sum +=n
print(even_sum)


# Day-5-4 Exercise

for n in range(1,101):
    if n % 3 ==0  and n % 5 == 0:
        print("FizzBuzz")
    elif n%3 ==0:
        print("Fizz")
    elif n%5 == 0:
        print("Buzz")
    else:
        print(n)            
    