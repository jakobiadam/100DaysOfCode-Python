from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for q in question_data:
    question_bank.append(Question(q["text"], q["answer"]))

questions = QuizBrain(question_bank)

while questions.still_has_questions():
    questions.next_question()

print("\nYou've completed the quiz!")
print(f"Your final score was {questions.score}/{len(questions.question_list)}")