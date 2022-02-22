mySet = {'a','b','c','d','e'}
item = input("Enter item :")
mySet.remove(item) if item in mySet else print(item," doesn't exist")
print(mySet)