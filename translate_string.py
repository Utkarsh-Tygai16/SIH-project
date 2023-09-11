# to translate the text from one language to another w/o language detection

'''
use cases :
- translating sentences
'''
import googletrans
from googletrans import *

trans = googletrans.Translator()

languages_list = googletrans.LANGUAGES

# print(languages_list['de'])

# ---------------------------------------- translation part :

string1 = "my name is aditya."

new_string = trans.translate(string1, dest="ko")
print(new_string.text)

# ---------------------------------------- detection part :

string2 = "Dies ist ein Auto"

detected_lang = trans.detect(string2)
print(detected_lang.lang) # this only gives out the ISO-639 code
# for the whole language name
print(f"the language detected is {languages_list[detected_lang.lang]}")

string3 = "billo balle baggeya da ki karegi"
print(trans.detect(string3))

# the confidence of the language detection is :

level_of_confidence = trans.detect(string3).confidence * 100
level_of_confidence = round(level_of_confidence, 2)
print(f"{level_of_confidence}%")

print(f"confidence of detection is {level_of_confidence}%")

    