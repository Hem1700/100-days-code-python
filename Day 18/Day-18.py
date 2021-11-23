from turtle import Turtle, Screen, right
import random
import turtle
# import heroes  pip install heroes
#Alias any model
# import turtle as t

tim = Turtle()

# Challange 1
for i in range(4):
    tim.forward(100)
    tim.left(90)



# Challange 2
for i in range(15):
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()


# Challange 3
def draw_shape(num_of_side):
    angle = 360/num_of_side
    for i in range(num_of_side):
        tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        tim.forward(100)
        tim.left(angle)
    

for i in range(3,11):
    draw_shape(i)




# Challange 4
directions = [0,90,180,270]
for _ in range(200):
    tim.speed("fastest")
    tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
    tim.pensize(5)
    tim.forward(30)
    tim.setheading(random.choice(directions))

screen = Screen()
screen.colormode(255)


# Challange 5
tim.speed("fastest")
def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
        tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
        tim.circle(100)
        tim.setheading(tim.heading()+size_of_gap)


draw_spirograph(5)


screen.exitonclick()