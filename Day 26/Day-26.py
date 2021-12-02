# List and Dictionary comprehensions

# new_list = [new_item for item in list]

# Example
# numbers = [1,2,3]
# new_list = [ n+1 for n in numbers]
# print(new_list)

# new_list = [num*2 for num in range(1,5)]

# new_list = [new_item for item in list if test]

import random
from turtle import st

# Day-26-1 Exercise

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [number*number for number in numbers]
print(squared_numbers)


# Day-26-2 Exercise
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)


# Day-26-3 Exercise

with open('file1.txt') as file1:
    contents1 = file1.read().split('\n')
    print(contents1)

with open('file2.txt') as file2:
    contents2 = file2.read().split('\n')
    print(contents2)


common_list = [number for number in contents1 if number in contents2]
print(common_list)

# states_not_guessed = list(set(state_names) - set(guessed_states))
# states_to_learn_dict = {
#     "States" :  states_not_guessed
# }

# data = pandas.DataFrame(states_to_learn_dict)
# data.to_csv("states_to_learn.csv")


# Dictionary Comprehensions

# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}


names = ['Alex', 'Beth', 'Caroline', 'Dave', 'Eleanor', 'Freddie']
student_score = {student: random.randint(1, 100) for student in names}
print(student_score)


passed_student = {student_name: score for (
    student_name, score) in student_score.items() if score > 60}
print(passed_student)


# Day-26-4 Exercise

sentence = "What is the Airspeed Velocity of an Unladen Swallow ?"
word_list = sentence.split(' ')
result = {word: len(word) for word in word_list}
print(result)


# Day-26-5 Exercise
weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
weather_f = {day: (temp * 9.0/5.0) + 32.0 for (day, temp) in weather_c.items()}
print(weather_f)

# Loop through pandas dataframe
student_dict = {
    "student": ["Hem", "Ishika", "Jigna", "Dharmesh"],
    "score": [90, 80, 100, 120],
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)
import pandas

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# # Loop through dataframe
# for key,value in student_data_frame.items():
#     print(key)
#     print(value)

# Loop through rows of dataframe

for (index, row) in student_data_frame.iterrows():
    print(row.student)