from data import GenerateQuestionBank
from quiz_brain import QuizBrain

question_bank = GenerateQuestionBank().question_bank

Quiz = QuizBrain(question_bank)
while Quiz.still_has_questions():
    Quiz.next_question()

print("You have completed the quiz!")
print(f"Your final score is {Quiz.score}/{Quiz.question_number}")


