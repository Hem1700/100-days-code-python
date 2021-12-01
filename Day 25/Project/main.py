import pandas
import  turtle

screen = turtle.Screen()
screen.title("U.S. States Game")
image =  "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv('50_states.csv')

state_names = data['state'].to_list()
guessed_states = []

while  len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct", prompt="What's another state's name?").title()
    if answer_state == 'Exit':
        break
    if answer_state in state_names:
        guessed_states.append(answer_state)
        name = turtle.Turtle()
        name.hideturtle()
        name.penup()
        state_data = data[data.state == answer_state]
        name.goto(int(state_data.x) , int(state_data.y))
        name.pendown()
        name.write(answer_state)


states_not_guessed = list(set(state_names) - set(guessed_states))
states_to_learn_dict = {
    "States" :  states_not_guessed
}

data = pandas.DataFrame(states_to_learn_dict)
data.to_csv("states_to_learn.csv")














# def get_mouse_click_cord(x,y):
#     print(x,y)



# turtle.onscreenclick(get_mouse_click_cord)
# turtle.mainloop()



