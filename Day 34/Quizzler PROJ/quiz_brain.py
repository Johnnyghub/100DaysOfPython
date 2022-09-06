from data import question_data
from question_model import Question


class QuizBrain:
    def __init__(self):
        self._question_number = -1
        self._questions_list = [Question(question["question"], question["correct_answer"]) for question in question_data]
        self._score = 0

    def moreQuestionsLeft(self):
        return self._question_number+1 < len(self._questions_list)

    def nextQuestion(self):
        self._question_number += 1
        return f"Q{self._question_number+1}. {self._questions_list[self._question_number].getQuestion()}"

    def check_answer(self, ans):
        if ans == self._questions_list[self._question_number].getAnswer().lower():
            return True  # correct
        else:
            return False  # incorrect

    def inc_and_return_score(self):
        self._score += 1
        return self._score
