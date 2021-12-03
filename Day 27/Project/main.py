from tkinter import *


window = Tk()

window.title("Mile to Km converter")
window.minsize(width=400 , height= 200)
window.config(padx= 100, pady= 50)

def button_clicked():
    miles = int(input.get())
    km = float(miles * 1.609)
    km_label.config(text = km)


# text
input = Entry(width=10)
input.get()
input.grid(column=1, row=1)

# label
mile_lable = Label(text='Miles')
mile_lable.grid(column=2, row=1)

#label
equal = Label(text="is equal to")
equal.grid(column=0, row=2)

# text
km_label = Label(text='0')
km_label.grid(column=1, row=2)

#label
label = Label(text='Km')
label.grid(column=2, row=2)


# button
button = Button(text= 'Calculate' , command= button_clicked)
button.grid(column=1, row=3)














window.mainloop()