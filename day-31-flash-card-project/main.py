from tkinter import *
import pandas, random

BACKGROUND_COLOR = "#B1DDC6"

# -------------------- Generate Random Telugu Words ---------------- #
data = pandas.read_csv("data/telugu_words.csv")
data_df = pandas.DataFrame(data)
data_list = data_df.values.tolist()

def generate_random_word():
    card_front.itemconfig(title_text, text="")
    card_front.itemconfig(title_text, text="Telugu")

    random_word = random.choice(data_list)
    card_front.itemconfig(word_text, text="")
    card_front.itemconfig(word_text, text=random_word[0])

# -------------------- UI SETUP ---------------- #

window = Tk()
window.title("Flashy")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

card_front = Canvas(width=800, height=526, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_front.create_image(400, 263, image=card_front_img)
card_front.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title_text = card_front.create_text(400, 150, text="Title", font=("Ariel", 40, "italic"))
word_text = card_front.create_text(400, 263, text="Word", font=("Ariel", 60, "italic"))
card_front.grid(column=0, row=0, columnspan=2)

#
# telugu_title = Label(text="Telugu", font=("Ariel", 40, "italic"))
# telugu_title.grid(column=0, row=0, columnspan=2)
#
# telugu_word = Label(text="cheppara zuk", font=("Ariel", 60, "bold"))
# telugu_word.grid(column=0, row=1, columnspan=2)

wrong_img = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, command=generate_random_word)
wrong_button.grid(column=0, row=1)

right_img = PhotoImage(file="images/right.png")
right_button = Button(image=right_img, highlightthickness=0, command=generate_random_word)
right_button.grid(column=1, row=1)



window.mainloop()