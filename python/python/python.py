import json
from difflib import get_close_matches

data = json.load(open("data.json", "r"))

def dict1(w):
    w = w.lower()
    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.title()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        print(f"Did you mean {''.join(get_close_matches(w,data.keys())[0])} ?")
        reply = input("Enter Y for Yes or N  for No:")
        reply = reply.upper()
        if reply == "Y":
            return data[get_close_matches(w, data.keys())[0]]
        elif reply == "N":
            return 'We did not understand the entry!'

        else:
            return 'Your message is unclear.Please double check it!'
    else:
        return 'The word does not exist.Please double check it!'

def lookup():
    word = input('Enter any word to get explanation of it:\n ')
    a = dict1(word)
    if type(a) == list:
        for i in a:
            print(i)
    else:
        print(a)

while True:
    lookup()
    a = input('Do you want to find information about another word?(Press Y to continue)')
    if a.upper() != 'Y':
        break

print('Program has been terminated')
