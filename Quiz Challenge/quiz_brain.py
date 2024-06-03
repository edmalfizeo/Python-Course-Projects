class QuizBrain:
    def __init__(self, q_list):
        self.q_nubmer = 0
        self.score = 0
        self.q_list = q_list

    def next_question(self):
        user_answer = input(f"Q.{self.q_nubmer + 1}: {self.q_list[self.q_nubmer].text} (True/False)?:  ")
        self.check_answer(user_answer, self.q_list[self.q_nubmer].answer)
        self.q_nubmer += 1

    def still_has_question(self):
        while self.q_nubmer < len(self.q_list):
            self.next_question()

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            self.score += 1
            print("You got it!")
        else:
            print("You are Wrong")
            print(f"The correct answer is {correct_answer}")
        print(f"You got {self.score}/{self.q_nubmer + 1} points so far!")
        print("\n")

    def total_score(self):
        return self.score





