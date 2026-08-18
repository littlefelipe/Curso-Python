import tkinter

window = tkinter.Tk()
window.title("My first GUI program")
window.minsize(width=1080, height=720)
window.config(padx= 100, pady= 100)

def button_clicked():
    my_label["text"] = input.get()
    print("CLICK!")

my_label = tkinter.Label(text="Label", font=("Arial", 24, "bold"))
my_label["text"] = "new text"
my_label.config(text="config text")
my_label.grid(column= 0,row= 0)



button2 = tkinter.Button(text="new button", command=button_clicked)
button2.grid(column=2, row=0)

button = tkinter.Button(text="click me", command=button_clicked)
button.grid(column=1, row=1)

input = tkinter.Entry()
input.grid(column=3, row=3)



window.mainloop()