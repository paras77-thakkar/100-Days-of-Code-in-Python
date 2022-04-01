class QuizBrain:
    def __init__(self, q_list):
        self.question_no = 0
        self.question_list = q_list
        self.score = 0

    def next_question(self):
        question = self.question_list[self.question_no]
        self.question_no += 1
        user_ans = input(f"Q{self.question_no}. {question.text} (True/False):")
        self.check_answer(user_ans, question.answer)

    def still_has_question(self):
        if self.question_no < len(self.question_list):
            return True
        else:
            return False

    def check_answer(self, user_ans, answer):
        if user_ans.lower() == answer.lower():
            print("Right Answer")
            self.score += 1

        else:
            print("Wrong Answer")
        print(f"The correct answer is:{answer}")
        print(f"Your Current score is {self.score}/{self.question_no}")
