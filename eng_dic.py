import json
import difflib
from difflib import get_close_matches


#Global
data  = json.load(open("data.json"))


#dictionary program


def keyword(word):
    if word in data:
        return data[word] 
    elif len(get_close_matches(word, data.keys())) > 0:
        correction = input(f"Did you mean {get_close_matches(word, data.keys())[0]} insted? Enter Yes of No: ")
        if correction == "Yes".lower():
            return data[get_close_matches(word, data.keys())[0]]
        elif correction == "No".lower():
            return "This word doesn't exist. Plese enter again. "
        else:
            return "Please enter 'Yes' or 'No: "
    else:
        return "This word doesn't exist. Plese enter again."
    

while True:
    word = input("Enter a word or enter 'END' to quit: ").lower()
    output = (keyword(word))
    if word == 'end':
        print("Thanks!")
        break
    else:
        if type(output) == list:
            for item in output:
                print(item)
        else:
            print(output)