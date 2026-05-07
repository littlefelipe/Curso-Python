from Quiz.quiz_brain import QuizBrain
from question_model import Question
from data import question_data

question_bank = []

for item in question_data:
    question = Question(item['text'], item['answer'])
    question_bank.append(question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")