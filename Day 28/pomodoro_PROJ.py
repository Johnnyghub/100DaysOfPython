from tkinter import *
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

def resetTimer():
    global reps

    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer", fg=GREEN)
    checkmarks.config(text="")
    reps = 1


# ---------------------------- TIMER MECHANISM ------------------------------- #

def startTimer():
    global reps

    if reps % 8 == 0:
        countdown(LONG_BREAK_MIN*60)
        title.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        countdown(SHORT_BREAK_MIN*60)
        title.config(text="Break", fg=PINK)
    else:
        countdown(WORK_MIN*60)
        title.config(text="Work", fg=GREEN)

    reps += 1


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def countdown(count):
    global timer

    countdown_min = floor(count/60)
    countdown_sec = int(count % 60)

    if countdown_min < 10:
        countdown_min = f"0{countdown_min}"
    if countdown_sec < 10:
        countdown_sec = f"0{countdown_sec}"

    canvas.itemconfig(timer_text, text=f"{countdown_min}:{countdown_sec}")

    if count > 0:
        timer = window.after(1000, countdown, count-1)
    else:
        startTimer()
        work_sessions_done = ""
        for i in range(floor(reps/2)):
            work_sessions_done += "✔"
        checkmarks.config(text=work_sessions_done)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

title = Label(fg=GREEN, bg=YELLOW, text="Timer", font=(FONT_NAME, 35, "bold"))
title.grid(row=0, column=1)

canvas = Canvas(width=230, height=230, bg=YELLOW, highlightthickness=0)
tomato = PhotoImage(file='tomato.png')
canvas.create_image(115, 115, image=tomato)
timer_text = canvas.create_text(115, 133, text="00:00", fill="white", font=(FONT_NAME, 28, "bold"))
canvas.grid(row=1, column=1)

button = Button(text="Start", command=startTimer, highlightthickness=0)
button.grid(row=2, column=0)

button = Button(text="Reset", command=resetTimer, highlightthickness=0)
button.grid(row=2, column=2)

checkmarks = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
checkmarks.grid(row=3, column=1)

window.mainloop()
