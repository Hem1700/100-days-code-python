from tkinter import *

window  = Tk()

def button_click():
    new_text  = input.get()
    my_label.config(text = new_text)

window.title("My First GUI Program")
window.minsize(width=500 , height= 300)
window.config(padx = 20 , pady= 20)

#Label
my_label = Label(text= "I am a label", font=("Arial", 20 , "normal"))
#my_label.pack(expand=True)  # Places the label in the screen and place it at the center of the screen
#my_label.pack()
#my_label.place(x=100, y=200)
my_label.grid(column= 0 ,row= 0)
# my_label["text" ] = "New Text"
# my_label.config(text = "Another New Text")
 
# button 
button = Button(text= 'Click me' , command= button_click)
new_button = Button(text= 'New button')
button.grid(column=1, row=1 )
new_button.grid(column=2, row=0)
# button.pack()

# Entry Component
input = Entry(width=10)
input.get()
input.grid(column=3, row=3)
# input.pack()


window.mainloop()



# Tkinter layout Managers  : Pack , Place and Grid
# Place = precise positioning x, y
# Grid = relative to other widgets



