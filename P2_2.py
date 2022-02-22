firstDictionary = {1:'a',2:'b',3:'c',4:'d',5:'e'}
secondDictionary = {6:'f',7:'g',8:'h'}
keys = list(secondDictionary.keys())
for i in keys:
    firstDictionary[i] = secondDictionary[i]
print(firstDictionary)