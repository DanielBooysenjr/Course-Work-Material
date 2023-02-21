from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
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

def save_info():
    website = website_entry.get()
    username = username_entry.get()
    password = password_entry.get()
    new_data = {website: {
                    "email": username,
                    "password": password
        }
    }

    if len(website) == 0 or len(password) == 0 or len(username) == 0:
        messagebox.showinfo(title="Oops", message="You can't have empty fields")
    else:
        try:
            # Open a file, that might or might nor exist
            with open("data.json", mode="r") as passwords:
                # Reading old data
                data = json.load(passwords)
        except FileNotFoundError:
            # If the file was not found, create the file
            with open("data.json", mode="w") as passwords:
                # Saving updated data
                json.dump(new_data, passwords, indent=4)
        else:
            # Updating old data with new data
            data.update(new_data)
            with open("data.json", "w") as passwords:
                json.dump(data, passwords, indent=4)
        finally:
            # Deleting entry fields
            website_entry.delete(0, END)
            password_entry.delete(0, END)
        
# ---------------------------- RETRIEVE SAVED PASSWORDS ------------------------------- #

def return_password():
    website_details = website_entry.get()
    try:
        with open("data.json", mode="r") as login_info:
            saved_websites = json.load(login_info)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No data file found.")
    else:
        if website_details in saved_websites:
            login_email = saved_websites[website_details]['email'] 
            login_password = saved_websites[website_details]['password']
            messagebox.showinfo(title="Login Information", message=f"Your Email is: {login_email}\nYour Password is: {login_password}")
        else:
            messagebox.showerror(title="No Entry Found", message=f"There is no details for {website_details.capitalize()}")

# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

# Adding the Logo
canvas = Canvas(window, width=200, height=200)
background = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=background)
canvas.grid(column=1, row=0)

# Creating the labels & Widgets
# # Website Label
website = Label(text="Website:")
website.grid(column=0, row=1)

# # Website Widget
website_entry = Entry(width=34)
website_entry.grid(column=1, row=1)
website_entry.focus()
website_entry.get()

# # Search Button
search = Button(width= 15,text="Search", command=return_password)
search.grid(column=2, row=1)

# # E-mail / Username
username = Label(text="Email/Username:")
username.grid(column=0, row=2)
# # Username Widget
username_entry = Entry(width=54)
username_entry.grid(column=1, row=2, columnspan=2)
username_entry.insert(0, "danielboysenjr@gmail.com")

# # Password
password = Label(text="Password:")
password.grid(column=0, row=3)
# # Password Widget
password_entry = Entry(width=35)
password_entry.grid(column=1, row=3)
# # Generate Password Button
password_gen = Button(text="Generate Password", command=generate_password)
password_gen.grid(column=2, row=3)

# Add Button
add = Button(text="Add", width=45, command=save_info)
add.grid(column=1, row=4, columnspan=2)


window.mainloop()