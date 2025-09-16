class quizzers:
    def __init__(self, ques_bank):
        self.ques_num = 0
        self.ques_bank = ques_bank
        self.point = 0
    def current_ques(self):
        user_input = input(self.ques_bank[self.ques_num].question)
        self.check_answer(user_input, self.ques_bank[self.ques_num].answer)
        self.ques_num += 1
    def connt(self):
        return [True if self.ques_num < len(self.ques_bank) - 1 else False]
    def check_answer(self, check_Anns, correct_ans):
        if check_Anns.lower() == correct_ans.lower():
            print("You got it right")
            self.point +=1
        else:
            print("You got it wrong")
    def score(self):
        print(f"Your Score is {self.point}")
        