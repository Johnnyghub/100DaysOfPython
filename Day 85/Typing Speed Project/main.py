import tkinter as tk
from tkinter import ttk
import random
from typing_test_data import paragraphs
import time

BACKGROUND_COLOR = "#B1DDC6"
start_time = 0  # this will be changed
random_text = ""

window = tk.Tk()  # declare here so we can declare these unchanging widgets
entry_box = ttk.Entry(window, font=('Courier', 12, 'normal'), width=50)
main_text = tk.Label(font=("Courier", 12, 'normal'), bg=BACKGROUND_COLOR,
                     wraplength=500, pady=25)  # these are the basic characteristics that don't change


# ----- Functions -------


def start_test():
    global start_button, start_time, main_text, entry_box, random_text
    random_text = random.choice(paragraphs)
    main_text.configure(text=random_text)  # change the text of the paragraph
    main_text.grid(column=1, row=1)

    entry_box.grid(column=1, row=2)  # we don't need to declare entry_box, we only hide and show it
    entry_box.focus_set()

    # when the user presses enter it calls this function, pass user and paragraph text
    entry_box.bind('<Return>', display_stats)

    start_time = time.time()  # get the time the user starts when they start typing
    start_button.grid_forget()  # hide the start button after the entry box is displayed


def display_stats(event):
    """Displays stats once the user presses enter and also displays the restart button"""
    global restart_button

    end_time = time.time() - start_time

    user_text = entry_box.get()

    correct_characters = 0
    for i, c in enumerate(random_text):  # iterate i as an integer to get index, and c as a character through the GUI text
        try:
            if user_text[i] == c:
                correct_characters += 1  # if they match add 1 to correct characters
        except:  # if user enters strings of different lengths, indexerrors or other may occur, pass for those since it is obviously incorrect
            pass

    accuracy = correct_characters * 100 / len(random_text)  # get the user's accuracy in %

    # using the english average word length of 4.7, we can calculate wpm as:
    wpm = (len(user_text) / (4.7 * end_time)) * 60  # multiply by 60 because otherwise it is words per second

    # change main text to display stats
    main_text.configure(text=f"Time: {round(end_time, 2)} seconds.\nAccuracy: {round(accuracy,1)}%\nWPM: {round(wpm,0)}.")

    # hide entry box
    entry_box.delete(0, 'end')  # delete the text from the box
    entry_box.unbind('<Return>')  # remove binding so you can't just spam enter
    entry_box.grid_forget()

    # show restart button
    restart_button.grid(column=1, row=3)


def restart_test():
    restart_button.grid_forget()
    start_test()

# ----- GUI ------


window.title("Typing Speed Tester")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=500, height=500)

window.columnconfigure(3)
window.rowconfigure(4)

title_label = tk.Label(text="Typing Speed Test", font=("Courier", 30, 'bold'), bg=BACKGROUND_COLOR, pady=25)
title_label.grid(column=1, row=0)

start_button = tk.Button(window, text="Start", font=('Courier', 12, 'bold'), command=start_test, padx=10, pady=10)
start_button.grid(column=1, row=1)

restart_button = tk.Button(window, text="Restart", font=('Courier', 12, 'bold'), command=restart_test, padx=10, pady=10)

window.mainloop()
