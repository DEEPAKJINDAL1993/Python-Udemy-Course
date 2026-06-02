from tkinter import *
import pandas
import random
BACKGROUND_COLOR = "#B1DDC6"


# ------------------------------- Load Data ------------------------------------ #

try:
    df = pandas.read_csv('data/words_to_learn.csv')
except FileNotFoundError:
    df = pandas.read_csv('data/french_words.csv')

to_learn = df.to_dict(orient='records')


current_card = {}


def next_card():
    global current_card
    global flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_image,image = card_front_image)
    canvas.itemconfig(card_title,text = 'French',fill = 'black')
    canvas.itemconfig(card_word, text=current_card['French'],fill = 'black')
    flip_timer = window.after(2000, flip_card)


def flip_card():
    canvas.itemconfig(card_image,image = card_back_image)
    canvas.itemconfig(card_title,text = 'English',fill='white')
    canvas.itemconfig(card_word,text = current_card['English'],fill='white')


def is_known():
    # df = df[df['French'] != current_card['French']]
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv('data/words_to_learn.csv',index=False)
    next_card()

# --------------------------------UI Setup-------------------------------------- #


window = Tk()
window.title("Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(2000, flip_card)

# Flash card canvas
canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR,highlightthickness=0)
card_front_image = PhotoImage(file="images/card_front.png")
card_back_image = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_image)
card_title = canvas.create_text(400,150,text="Title",font=("Ariel",40,"italic"), anchor=CENTER)
card_word = canvas.create_text(400,263,text = 'word',font=("Ariel",60,"bold"), anchor=CENTER)
canvas.grid(row=0,column=0,columnspan=2)

# Buttons
cross_image = PhotoImage(file="images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(row=1,column=0)

check_image = PhotoImage(file="images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(row=1,column=1)

next_card()


window.mainloop()



