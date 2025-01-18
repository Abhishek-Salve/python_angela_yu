from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for question in question_data:
    new_ques = Question(question["text"], question["answer"])
    question_bank.append(new_ques)

quiz_1 = QuizBrain(question_bank)
# print(quiz_1.question_number)
# print(quiz_1.question_list[0])
# print(quiz_1.next_question())

while quiz_1.question_pending():
    quiz_1.next_question()
    print("")

print("Quiz is complete !!")
print(f"Your final score was {quiz_1.score}/{len(question_bank)}")
