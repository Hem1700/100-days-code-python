 # functions with inputs

def greet(name):
    print(f"Hello {name}")
    print("How are you?")
    print("Take care")

greet("Hem")


def greet_with(name, location):
    print(f"Hello {name}")
    print(f"How's the wheather in {location}?")



greet_with("Hem", "India")
greet_with(location= "India", name="Hem")



# Day-8-1  Exercise
import math
test_h = int(input("Height of the wall: "))
test_w = int(input("Width of the wall: "))
coverage = 5

def paint_calc(height, width, cover):
    cans = math.ceil((height* width)/coverage)
    print(cans)


paint_calc(height= test_h, width= test_w, cover= coverage)



# Day-8-2 Exercise

def prime_checker(n):
    is_prime = True
    for i in range(2, n):
        if n % i == 0 :
            is_prime = False
    if is_prime == True:
        print("It is a prime number")
    else:
        print("It is not a prime number")        

n = int(input("Check this number : "))
prime_checker(n)

        