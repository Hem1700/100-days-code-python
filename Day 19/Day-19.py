from turtle import Turtle , Screen

tim = Turtle()
screen = Screen()


def mov_forward():
    tim.forward(10)

screen.listen()
screen.onkey(key="space", fun = mov_forward)
screen.exitonclick()



# Object State and Instances

red = Turtle()
blue = Turtle()
green = Turtle()
