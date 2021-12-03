# Advanced Arguments
# Argument with default values
from typing import KeysView


def my_function(a=1,b=2,c=4):
    pass
my_function()

# Unlimited Positional Arguments

def add(*args):   # args is a tuple
    sum = 0
    for n in args:
        sum += n
    print(sum)

add(2,4)



# Many keyworded arguments
# **kwargs

def calculate(n,**kwargs):  # kwargs is a dictionary
    print(kwargs)
    # for key,value in kwargs.items():
    #     print(key)
    #     print(value)
    n += kwargs['add']
    n *= kwargs['multiply']
    print(n)

    

calculate(2, add = 3, multiply = 5)



class Car:

    def __init__(self, **kwargs):
        self.make = kwargs.get('make')
        self.color = kwargs.get('color')
        self.model = kwargs.get("model")  # if the key doesnt exists then it returns none


my_car = Car(make = 'Nissan')
 