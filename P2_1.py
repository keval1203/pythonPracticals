myDictionary = {1:'a',2:'b',3:'c',4:'d'}
keys = list(myDictionary.keys())
key = int(input("Enter key :"))
print(key," already exists") if key in keys else print(key," doesn't exist")
