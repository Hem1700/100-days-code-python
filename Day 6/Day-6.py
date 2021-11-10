print("Hello")


def my_function():
    print("This is my function")


my_function()


# While loop
n = 1
while n > 0:
    print("Hello")


# Solution for hurdle 3

def turn_right():
    for i in range(0,3):
        turn_left()
    
   
def wall():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    
    
def front():
    turn_left()
    move()
    
    
    
    
while not at_goal():     
    if wall_in_front():
        wall()
        turn_left()
    else:
        move()
        


# Solution for hurdle 4

def turn_right():
    for i in range(0,3):
        turn_left()
def jump():
    turn_left()
    while wall_on_right():
        move()
    turn_right()
    move()
    turn_right()   
    while front_is_clear():
        move()
    turn_left()                          
while not at_goal():
    if wall_in_front():
        jump()                            
    else:
        move()
   
      