from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    text = question['text']
    answer = question['answer']
    new_question = Question(text, answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

quiz.still_has_question()

print(f"You got a total of {quiz.total_score()}/12 points")
print("Thank you for playing!")

