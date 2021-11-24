from turtle import Turtle , Screen, screensize

tim = Turtle()
screen = Screen()

def mov_forward():
    tim.forward(20)

def move_backword():
    tim.backward(20)

def turn_right():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)

def turn_left():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()
    

screen.listen()
screen.onkey(key="w", fun = mov_forward)
screen.onkey(key="s", fun= move_backword)
screen.onkey(key="a", fun= turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun= clear_screen)
screen.exitonclick()