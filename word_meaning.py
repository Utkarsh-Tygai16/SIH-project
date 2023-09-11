# the api to be used :
# https://api.dictionaryapi.dev/api/v2/entries/en/<word>


import requests

#--------------------------------availability of the word :

def valid(word) :

    wordDictionary = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    if wordDictionary.status_code == 404 :
        print(f"{word} is not a valid word.Please enter valid input.")
    else :
        print("valid word")
        pass

# valid("audbhbyubyub")

#--------------------------------availability of the word :


def meanings(word) :
    wordDictionary = requests.get(f"https://api.dictionaryapi.dev/api/v2/entries/en/{word}")

    wordDictionary = wordDictionary.json()
    # here the api is converted into json format
    wordDictionary = wordDictionary[0]
    # here the wordDictionary is now just a dictionary with all the properties of the word

    word_partOfSpeech = wordDictionary['meanings'][0]["partOfSpeech"]
    word_meaning = wordDictionary['meanings'][0]["definitions"][0]["definition"]
    word_synonyms = wordDictionary['meanings'][0]["synonyms"] # this is a list of synonyms

    word_dict = {
        "meaning" : word_meaning,
        "part" : word_partOfSpeech,
        "synonyms" : word_synonyms
    }

    return word_dict

#-----------------------------------------------------------test :

word = "audacity"

valid(word)
print(f"meaning of {word} is '{meanings(word)['meaning']}'")
print(f"part of speech of {word} is '{meanings(word)['part']}'")
print(f"synonyms of {word} are :")

for i in meanings(word)['synonyms'] :
    print(i) # synonym