import json

from difflib import get_close_matches

data= json.load(open("076 data.json",'r'))

def give(w):
    w = w.lower()
    if w in data:
      return data[w]
    elif w.title() in data:
      return data[w.title()]
    elif w.upper() in data:   
      return data[w.upper()]
    elif len(get_close_matches(w,data.keys(),cutoff=0.8)) > 0:
      reply = input("Did you mean %s instead ? Enter Y if yes and N if No " % get_close_matches(w,data.keys(),cutoff= 0.8)[0])
      if reply == "Y" :
        return data[get_close_matches(w,data.keys(),cutoff=0.8)[0]]
      elif reply == "N" :
        return ("This word does not exist in the data. Please double check it")
      else:
        return ("We did not understand your reply. Please double check it")
       
    else:
      return ("This word does not exist in the data")

word = input("Enter a word : ")

output = give(word)

if type(output) == list:
  for item in output:
    print(item)
else:
  print(output)
 

