from tkinter import *

def button_clicked():
    result.config(text= miles_to_km())

def miles_to_km():
    mile = float(input.get())
    kilometer = mile * 1.609
    return kilometer

window = Tk()
window.title("Mile to Km Converter")
window.minsize(width=1080, height=720)
window.config(padx= 100, pady= 100)

miles = Label()
miles.config(text="Miles", font=("Times New Roman", 24))
miles.grid(column=3, row=0,)

km = Label()
km.config(text="Km",font=("Times New Roman", 24))
km.grid(column= 3, row=1)

label = Label()
label.config(text="is equal to",font=("Times New Roman", 24))
label.grid(column=1, row=1)

result = Label()
result.config(text= "0",font=("Times New Roman", 24))
result.grid(column=2, row=1)

input = Entry()
input.grid(column=2, row=0)

button = Button(text="Convert", command=button_clicked)
button.grid(column=2, row=2)

window.mainloop()