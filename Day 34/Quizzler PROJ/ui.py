from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=30, pady=30, bg=THEME_COLOR)

        CHECK = PhotoImage(file='images/true.png')
        CROSS = PhotoImage(file='images/false.png')

        self.score_label = Label(text="Score: 0", fg='white', bg=THEME_COLOR, font=("Arial", 13, 'bold'))
        self.score_label.grid(row=0, column=1)

        self.canvas = Canvas(width=300, height=250, borderwidth=0, highlightthickness=0, bg='white')
        self.question = self.canvas.create_text(150, 125, text="", font=("Arial", 20, "italic"), fill=THEME_COLOR, width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)

        self.true_button = Button(image=CHECK, command=self.true_pressed, highlightthickness=0, borderwidth=0, activebackground=THEME_COLOR)
        self.true_button.grid(row=2, column=0)

        self.false_button = Button(image=CROSS, command=self.false_pressed, highlightthickness=0, borderwidth=0, activebackground=THEME_COLOR)
        self.false_button.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.moreQuestionsLeft():
            q_text = self.quiz.nextQuestion()
            self.canvas.itemconfig(self.question, text=q_text)
        else:
            self.canvas.itemconfig(self.question, text="You've reached the end of the quiz! Check your score out of 10 in the top right.")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_pressed(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, correct: bool):
        if correct:
            self.score_label.config(text=f"Score: {int(self.quiz.inc_and_return_score())}")
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)
