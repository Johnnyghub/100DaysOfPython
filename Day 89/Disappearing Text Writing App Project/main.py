from tkinter import *
import time

BACKGROUND_COLOR = "#B1DDC6"
time_since_last_keystroke = time.time()  # this function saves when the user last typed

# ------------- FUNCTIONS ----------------


def reset_timer():
    global time_since_last_keystroke
    time_since_last_keystroke = time.time()


def delete_text():
    global time_since_last_keystroke, entry_box
    if time.time() - time_since_last_keystroke >= 5:
        try:
            entry_box.delete('1.0', 'end')  # delete the text from the box
            time_since_last_keystroke = time.time()  # this prevents the delete function from running non stop, doesn't affect function of the app but may stop text from being deleted twice after the user stops typing
        except TclError:  # text box is empty when you try to delete, this shouldn't happen but I feel like it's hardware related as it is random
            pass
    window.after(100, delete_text)  # rerun this command every 100 milliseconds, or 0.1 seconds


# ------------- GUI ----------------------


window = Tk()
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
window.minsize(width=400, height=400)

window.columnconfigure(3)
window.rowconfigure(3)

title_label = Label(text="Disappearing Text App", font=("Courier", 30, 'bold'), bg=BACKGROUND_COLOR, pady=25)
title_label.grid(column=1, row=0)

description_label = Label(text="If you stop typing for 5 seconds, all your text will disappear!", font=("Courier", 15, 'bold'), bg=BACKGROUND_COLOR, pady=25)
description_label.grid(column=1, row=1)

entry_box = Text(window, font=('Courier', 12, 'normal'), width=50)
entry_box.bind("<KeyPress>", lambda e: reset_timer())  # everytime text is entered, reset timer
entry_box.grid(column=1, row=2)

delete_text()

window.mainloop()

