class Question:
    def __init__(self, text, answer):
        self._text = text
        self._answer = answer

    def getAnswer(self):
        return self._answer

    def getQuestion(self):
        return self._text
