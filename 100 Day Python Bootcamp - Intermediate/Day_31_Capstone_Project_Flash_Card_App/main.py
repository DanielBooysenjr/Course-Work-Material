from tkinter import *
import pandas
import random

# # ---------------- FLASH CARD PROJECT ---------------- # #

# # ---------------- CHANGING THE WORDS ---------------- # #

random_word = {}
to_learn = {}
# def french_words():
try:
    data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    data_dict = original_data.to_dict(orient="records")
else:
    # to_learn = data.to_dict(orient="records")
    data_dict = data.to_dict(orient="records")

def generate_word():
    global random_word, flip_timer
    window.after_cancel(flip_timer)
    random_word = random.choice(data_dict)
    front_of_card.itemconfig(card_title, text="French", fill="black")
    front_of_card.itemconfig(card_word, text=random_word["French"], fill="black")
    front_of_card.itemconfig(card_background, image=front_image)
    flip_timer = window.after(3000, func=flip_card)


def flip_card():
    front_of_card.itemconfig(card_title, text="English", fill="white")
    front_of_card.itemconfig(card_word, text=random_word["English"], fill="white")
    front_of_card.itemconfig(card_background, image=card_back_image)

def is_known():
    data_dict.remove(random_word)
    print(len(data_dict))
    data = pandas.DataFrame(data_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    generate_word()

# # ---------------- USER INTERFACE ---------------- # #
BACKGROUND_COLOR = '#B1DDC6'

window = Tk()
window.title("Language Learning - Flash Card App")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)


# # Front of Card
front_of_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_background = front_of_card.create_image(400,263, image=front_image)
front_of_card.grid(column=0, row=0, columnspan=2)
# Displaying text
card_title = front_of_card.create_text(400, 150, text="French", fill="black", font=("arial", 40, "italic"))
card_word = front_of_card.create_text(400, 263, text="word", fill="black", font=("arial", 60, "bold"))

# Back of Card
back_of_card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
back_image = PhotoImage(file="images/card_back.png")

# Adding Buttons
# # Wrong Button
wrong_button = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_button, highlightthickness=0, command=generate_word)
wrong.grid(column=0, row=1, padx=20, pady=20)

# # Right Button
right_button = PhotoImage(file="images/right.png")
right = Button(image=right_button, highlightthickness=0, command=is_known)
right.grid(column=1, row=1, padx=20, pady=20)

generate_word()



window.mainloop()