import json
from difflib import get_close_matches

data = json.load(open("file.json"))

def translate(word):
    if word.lower() in data:
        return (data[word.lower()])
    elif len(get_close_matches(word, data.keys())) > 0:
        print("Did you mean %s instead?" % get_close_matches(word, data.keys())[0])
        response = input("Enter Y for yes and N for no: ")
        if response == "Y":
            return (data[get_close_matches(word, data.keys())[0]])
        elif response == "N":
            return ("Word not found")
        else:
            return ("Invalid input")
    else:
        return ("Word not found")


word = input("Enter word: ")
result = translate(word)

if type(result) == list:
    for item in result:
        print(item)
else:
    print(result)