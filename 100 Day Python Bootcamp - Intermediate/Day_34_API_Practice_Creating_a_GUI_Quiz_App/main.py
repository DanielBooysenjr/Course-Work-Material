from question_model import Question
# from data import question_data
from quiz_brain import QuizBrain
import requests
from ui import QuizInterface


# Setting the parameters for the api request
paraments = {
    "amount": 10,
    "type": "boolean",
    "category": 18

}

# Connecting to the api
response = requests.get("https://opentdb.com/api.php", params = paraments)
response.raise_for_status()
# Storing the data in a variable called question data
data = response.json()

question_data = (data["results"])

question_bank = []
for results in question_data:
    question_text = results["question"]
    question_answer = results["correct_answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)


print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
