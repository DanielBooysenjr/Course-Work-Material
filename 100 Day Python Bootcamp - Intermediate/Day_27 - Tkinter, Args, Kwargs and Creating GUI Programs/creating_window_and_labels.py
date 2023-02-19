# Creating a window and labels

from tkinter import *

# Create window
window = Tk()
window.title("First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Creating a label
my_label = Label(text="I am a label", font=("courier", 12, "bold"))
my_label.grid(column=0, row=0)
my_label.config(padx=50, pady=50)

my_label["text"] = "New Text"
my_label.config(text="Hello Text")

# Creating a button

def button_clicked():
    my_label.config(text="I got clicked")
    

# Entry Component - Input

input = Entry(width=10)
input.grid(column=4, row=3)


def replace():
    my_label.config(text=input.get())

button = Button(text="I am a button", command=replace)
button.grid(column=2, row=2)

new_button = Button(text="New Button")
new_button.grid(column=3, row=1)



# Keeping window open
window.mainloop()