from tkinter import *
from random import choice
from pandas import read_csv, DataFrame

BACKGROUND_COLOR = "#B1DDC6"
CARD_POSITION = (400, 263)
current_card = {}
flipped = True

#------------- LOAD DATA --------------------#

try:  # see if words to learn exists, and use that one instead if it does
    words = read_csv('data/words_to_learn.csv', encoding="ISO-8859-1").to_dict('records')  # ISO encoding ?? why
    print("Existing data found.")
except FileNotFoundError:  # if not, load the entire french_words csv file since the user is starting from scratch
    words = read_csv("data/french_words.csv").to_dict('records')


#---------- Card Functionality ------------#

def random_word():
    global current_card, flipped
    if flipped:
        flipped = False  # prevent button spam from calling function before card is flipped
        current_card = choice(words)
        canvas.itemconfig(card, image=CARD_FRONT)
        canvas.itemconfig(language, text="French", fill="Black")
        canvas.itemconfig(word, text=current_card["French"], fill="Black")
        window.after(3000, func=flip_card)  # flip cards after 3 seconds


def flip_card():
    global flipped
    canvas.itemconfig(card, image=CARD_BACK)
    canvas.itemconfig(language, text="English", fill="White")
    canvas.itemconfig(word, text=current_card["English"], fill="White")
    flipped = True


def correct():
    global flipped
    if flipped:
        words.remove(current_card)  #if user guessed correctly, remove the card from the words dictionary
        random_word()


#------------- CONFIGURE UI -----------------#

window = Tk()
window.title("Flashy - French/English Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

CHECK = PhotoImage(file='images/right.png')
CROSS = PhotoImage(file='images/wrong.png')
CARD_FRONT = PhotoImage(file='images/card_front.png')
CARD_BACK = PhotoImage(file='images/card_back.png')

canvas = Canvas(width=800, height=526, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)
card = canvas.create_image(CARD_POSITION, image=CARD_FRONT)
language = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

correct_button = Button(image=CHECK, command=correct, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
correct_button.grid(column=0, row=1)

wrong_button = Button(image=CROSS, command=random_word, highlightthickness=0, borderwidth=0, activebackground=BACKGROUND_COLOR)
wrong_button.grid(column=1, row=1)

random_word()  # generate the first word

window.mainloop()

# after the window is closed

with open(file="data/words_to_learn.csv", mode="w") as file:
    data = DataFrame.from_dict(words)  # turn dict back into df
    data.to_csv(file, index=False, line_terminator="\n")  # write words not completed to a new file and load that next time
