
# try:
#     file = open('a.txt')
#     a_dict = {"key": "value"}
#     value = a_dict['key']
# except FileNotFoundError:
#     file = open('a.txt', 'w')
#     file.write('Something')
# except KeyError as errormessage:
#     print(errormessage)
# else:
#     content = file.read()
#     print(content)
# finally:
#     raise TypeError('This is an raised error')


# Raising Exceptions

# height = float(input('Height: '))
# weight = int(input('Weight: '))

# if height > 3:
#     raise ValueError('Human height should not be over 3m')

# bmi = weight/ height**2
# print(bmi)


# Day-30 Exercise 1

fruits = ["Apple", "Pear", "Orange"]

#TODO: Catch the exception and make sure the code runs without crashing.
def make_pie(index):
    try:
        fruit = fruits[index]
        
    except IndexError:
        print('Fruit pie')
    else:
        print(fruit + " pie")

make_pie(4)


# Day-30 Exercise 2

facebook_posts = [
    {'Likes': 21, 'Comments': 2}, 
    {'Likes': 13, 'Comments': 2, 'Shares': 1}, 
    {'Likes': 33, 'Comments': 8, 'Shares': 3}, 
    {'Comments': 4, 'Shares': 2}, 
    {'Comments': 1, 'Shares': 1}, 
    {'Likes': 19, 'Comments': 3}
]

total_likes = 0


for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass

      


print(total_likes)
