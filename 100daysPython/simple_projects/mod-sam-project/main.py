from data import questions_answers
from questions import Questions
from quizer import quizzers

questions_list = []

for ques in questions_answers:
    questions_text = ques["question"]
    answers_text = ques["answer"]
    new_ques = Questions(questions_text, answers_text)
    questions_list.append(new_ques)
    
quiz = quizzers(questions_list)
while quiz.connt()[0]:
    quiz.current_ques()
    quiz.score()

quiz.score()