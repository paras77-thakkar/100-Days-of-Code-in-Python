from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
question_bank = []             #takeing all the ques ans in list of object( Q1(Q,A))
for question in question_data:
    que = question["text"]
    ans = question["answer"]
    ques_ans = Question(que, ans)
    question_bank.append(ques_ans)

quiz= QuizBrain(question_bank)
while quiz.still_has_question():
    quiz.next_question()

print(f"Your final socre is {quiz.score}/{len(question_bank)}")
