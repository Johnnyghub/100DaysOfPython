from data import question_data
from question_model import Question


class QuizBrain:
    def __init__(self):
        self._question_number = 0
        self._questions_list = [Question(question["question"], question["correct_answer"]) for question in question_data]
        self._score = 0

    def moreQuestionsLeft(self):
        if self._question_number < len(self._questions_list):
            return True
        else:
            print(f"You've completed the quiz!\nYour final score is {self._score} out of {len(self._questions_list)}!")
            return False

    def nextQuestion(self):
        """Prints the next question, asks for user input, checks the answer, and then incremenets score if correct
         and the question number regardless. If EOL reached, return False."""
        ans = ""

        while ans == "":
            ans = input(f"Q{self._question_number + 1}. {self._questions_list[self._question_number].getQuestion()} (True/False)? ").lower()

            if ans != 'true' and ans != 'false':
                print("Please enter only true or false.\n")
                ans = ""

        if self.rightAnswer(ans):
            self._score += 1
            print(f"Correct! That was the right answer.\nYour current score is {self._score} out of "
                  f"{self._question_number+1}!\n")
        else:
            print(f"Incorrect. The right answer was {self._questions_list[self._question_number].getAnswer()}.\n"
                  f"Your current score is {self._score} out of {self._question_number+1}!\n")

        self._question_number += 1

    def rightAnswer(self, ans):
        if ans == self._questions_list[self._question_number].getAnswer().lower():
            return True  # correct
        else:
            return False  # incorrect
