import json
#--------library to compare texts--------#
import difflib
from difflib import SequenceMatcher
from difflib import get_close_matches

print(SequenceMatcher(None,"rainn","rain").ratio())
data= json.load(open("data.json"));
print(type(data))

def translate(word):
    word= word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:#if user entered "texas" this will check for "Texas" as well.
        return data[word.title()]
    elif word.upper() in data: #in case user enters words like USA or NATO
        return data[word.upper()]
    elif len(get_close_matches(word,data.keys()))>0:
        yn= input("Did you mean %s instead?" % get_close_matches(word,data.keys())[0])
        if(yn=='Y' or yn=='y'):
            return data[get_close_matches(word,data.keys())[0]]
        elif(yn=='N'or yn=='n'):
            return "word doesn't exist"
        else:
            return "We didn't understand your entry"
        
    
    else:
        return "Word doesn't exist"
ch="y"
while(ch=='Y' or ch=='y'):
    word= input("Enter the word: ")
    output=translate(word)
    if(type(output)== list):
        for out in output:
            print(out)
    else:
        print(output)
    
    ch=input("want to continue?")
    
