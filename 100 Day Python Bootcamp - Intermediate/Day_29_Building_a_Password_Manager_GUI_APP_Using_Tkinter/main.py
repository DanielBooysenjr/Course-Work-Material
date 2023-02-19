from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    password_entry.delete(0, END)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_numbers + password_symbols + password_letters
    shuffle(password_list)
    password ="".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
# Creating and writing to the file with the information passed in the info function
def save_info():
    with open("data.txt", mode="a") as passwords:
        passwords.write(info())
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# Obtaining the information that was placed inside the entry boxes
def info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="You can't have empty fields")
    else:

        is_ok = messagebox.askokcancel(title=website, message=f'These are the details entered: \nEmail: {username}'
                                                        f'\nPassword: {password} \nIs it okay to save?')
        if is_ok:
            save_info
        
        return f"Website: {website} \nUsername: {username} \nPassword: {password}\n\n"

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Adding the Logo
canvas = Canvas(window, width=200, height=200)
background = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background)
canvas.grid(column=1, row=0)

# Creating the labels & WidgetsS
# # Website Label
website = Label(text="Website:")
website.grid(column=0, row=1)

# # Website Widget
website_entry = Entry(width=54)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()
website_entry.get()
# # E-mail / Username
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
# # Username Widget
username_entry = Entry(width=54)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "")

# # Password
password = Label(text="Password:")
password.grid(column=0, row=3)
# # Password Widget
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)
# # Generate Password Button
generate_password = Button(text="Generate Password", command=generate_password)
generate_password.grid(column=2, row=3)

# Add Button
add = Button(text="Add", width=45, command=save_info)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()