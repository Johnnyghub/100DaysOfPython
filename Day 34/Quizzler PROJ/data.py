from requests import get
from html import unescape

# get 10 random questions everytime you run the program
with get(url="https://opentdb.com/api.php?amount=10&type=boolean") as response:
    response.raise_for_status()
    question_data = response.json()['results']


# unescape all the html encoding in the question (such as quotation marks)
for question in question_data:
    question['question'] = unescape(question['question'])
