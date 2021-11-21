from question_model import QuestionModel
from data import question_data
from quiz_model import QuizBrain

question_bank = []

for data in question_data:
    question_text = data['question']
    question_answer = data['correct_answer']
    new_question = QuestionModel(question_text, question_answer)
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)


while quiz.still_has_question():
    quiz.next_question()
    final_score = quiz.score

print("You've completed the quiz.")
print(f"Your final score is {final_score}/{quiz.question_number}")
