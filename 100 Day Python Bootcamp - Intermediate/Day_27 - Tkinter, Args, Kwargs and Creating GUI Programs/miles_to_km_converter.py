# Miles to KM Converted

from tkinter import *

# Calculation function
def calculate():
    calculated = float(input.get())
    total_km = calculated * 1.609344 
    total.config(text=round(total_km, 2))

window = Tk()
window.title("Mile to Km Converter")
window.minsize(300,100)
window.config(padx=20, pady=20)

# Input
input = Entry(width=10)
input.grid(column=1, row=0)

# Miles Test
miles = Label(text="Miles")
miles.grid(column=2, row=0)

# Is Equal to
equal = Label(text="is equal to: ")
equal.grid(column=0, row=1)

# Amount of Km lable
total = Label(text=0)
total.grid(column=1, row=1)
    
# Kilometer
km = Label(text="Km")
km.grid(column=2, row=1)

# Calculate
calculate = Button(text="Calculate", command=calculate)
calculate.grid(column=1, row=2)



window.mainloop()