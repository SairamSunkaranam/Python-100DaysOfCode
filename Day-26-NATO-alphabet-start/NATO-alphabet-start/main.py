student_dict = {
    "student": ["Angela", "James", "Lily"], 
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas
student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")

nato_dict = {row.letter: row.code for (index, row) in nato_data.iterrows()}


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

def generate_phenotic():
    word = input("Enter the Word: ").upper()
    try:
        nato_words = [nato_dict[letter] for letter in word]
    except KeyError:
        print("only alphabets in the word please")
        generate_phenotic()
    else:
        print(nato_words)

generate_phenotic()


