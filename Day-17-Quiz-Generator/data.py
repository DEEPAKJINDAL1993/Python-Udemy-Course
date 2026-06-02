import requests
from question_model import Question
import html
import json

question_data_backup = [
    {"text": "A slug's blood is green.", "answer": "True"},
    {"text": "The loudest animal is the African Elephant.", "answer": "False"},
    {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
    {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
    {"text": "In West Virginia, USA, if you accidentally hit an animal with your car,"
             " you are free to take it home to eat.", "answer": "True"},
    {"text": "In London, UK, if you happen to die in the House of Parliament, "
             "you are entitled to a state funeral.", "answer": "False"},
    {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
    {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
    {"text": "Google was originally called 'Backrub'.", "answer": "True"},
    {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
    {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
    {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
]
category = {
    1 : "General Knowledge",
    2: "Books",
    3: "Film",
    4: "Music",
    5: "Musicals and Theatres",
    6: "Television",
    7: "Video Games",
    8: "Board Games",
    9: "Science and Nature",
    10: "Computers",
    11: "Mathematics",
    12: "Mythology",
    13: "Sports",
    14: "Geography",
    15: "History",
    16: "Politics",
    17: "Art",
    18: "Celebrities",
    19: "Animals"
}

class GenerateQuestionBank:
    def __init__(self):
        ''' Generates a question bank for selected  number of questions and difficulty level'''
        self.number_of_questions = int(input("How many questions do you want in the quiz: "))
        self.difficulty = input("Select difficulty (hard/medium/easy): ").lower()
        for i in category:
            print(f"{i}: {category[i]}")
        self.quiz_category = str(int(input("Type 1 to 19 for required category: "))+8)
        self.url = ('https://opentdb.com/api.php?amount=' + str(self.number_of_questions)
                    + '&category=' + str(self.quiz_category)
                    + '&difficulty=' + self.difficulty
                    + '&type=boolean')
        print(self.url)
        self.question_data = requests.get(self.url).json()['results']
        self.question_bank = []
        for question in self.question_data:
            self.question_bank.append(Question(html.unescape(question['question']), html.unescape(question['correct_answer'])))

#url = 'https://opentdb.com/api.php?amount=10&type=boolean'
#url = 'https://opentdb.com/api.php?amount=10&category=22&difficulty=medium&type=boolean'
#response = requests.get(url)

