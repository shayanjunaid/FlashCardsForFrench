from tkinter import *
from data import *
from random import *
from pandas import *

wait = ""
french_word = ""
english_word = ""
correct_words = []


def save_data():
    to_learn = {"French": {}, "English": {}}
    for i in range(len(words["French"])):
        if words["French"][i] not in correct_words:
            to_learn["French"][i] = words["French"][i]
            to_learn["English"][i] = words["English"][i]
    df = DataFrame(to_learn)
    df.to_csv("words_to_learn.csv", index=False)


def flip_card():
    card.create_image(400, 260, image=card_ans_side)
    language_label.config(text="English", bg=CARD_BACK_COLOR, fg=CARD_FRONT_COLOR)
    word_label.config(text=english_word, bg=CARD_BACK_COLOR, fg=CARD_FRONT_COLOR)


def new_card():
    global french_word
    global english_word
    random_choice = randint(0, len(words["French"]))
    french_word = words['French'][random_choice]
    english_word = words['English'][random_choice]
    if random_choice not in used_words:
        card.create_image(400, 260, image=card_qes_side)
        language_label.config(text="French", bg=CARD_FRONT_COLOR, fg=CARD_BACK_COLOR)
        word_label.config(text=french_word, bg=CARD_FRONT_COLOR, fg=CARD_BACK_COLOR)
        window.after(3000, flip_card)


def answer_correct():
    correct_words.append(french_word)
    save_data()
    new_card()


def answer_wrong():
    new_card()


BG_COLOR = "#59FAAE"
CARD_FRONT_COLOR = "white"
CARD_BACK_COLOR = "#91c2af"

window = Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BG_COLOR)

# Photoimages

tick = PhotoImage(file="right.png")
card_qes_side = PhotoImage(file="card_front.png")
card_ans_side = PhotoImage(file="card_back.png")
cross = PhotoImage(file="wrong.png")

# card

card = Canvas(width=800, height=520, highlightthickness=0, bg=BG_COLOR)
card.create_image(400, 260, image=card_qes_side)
card.grid(row=0, column=0, columnspan=2, rowspan=2)

# correct button

correct_button = Button(image=tick, highlightthickness=0, command=answer_correct)
correct_button.grid(row=2, column=1)

# wrong button

wrong_button = Button(image=cross, highlightthickness=0, command=answer_wrong)
wrong_button.grid(row=2, column=0)

# language label

language_label = Label(text="Language", font=("Arial", 60, "bold"), bg=CARD_FRONT_COLOR)
language_label.grid(row=0, column=0, columnspan=2)

# word label

word_label = Label(text="Word", font=("Arial", 40, "normal"), bg=CARD_FRONT_COLOR)
word_label.grid(row=0, column=0, columnspan=2, rowspan=2)

new_card()
window.mainloop()
