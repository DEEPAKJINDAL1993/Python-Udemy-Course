student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pd.read_csv("nato_phonetic_alphabet.csv")
# print(type(df))
# print(df)

phonetics = {row.letter:row.code for (index, row) in df.iterrows()}
# print(phonetics)


# TODO 2. Create a list of the phonetic code words from a word that the user inputs.
def phonetic():

    user_input = input("Enter a word: ").upper()
    letters = [word for word in user_input]
    print(letters)

    try:
        result = [phonetics[letter] for letter in letters]
    except KeyError:
        print("Sorry, please enter only alphabets")
        phonetic()
    else:
        print(result)


phonetic()
