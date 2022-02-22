myList = ['a','b','a','c','d','a']
myTuple = (1,2,3,4,3,5,3,3)
myDictionary = {1:'x',2:'y',3:'x',4:'z'}
def mostCommonItem(list):
    count = 0
    item = list[0]
    for i in list:
        frequency = list.count(i)
        if frequency>count:
            count = frequency
            item = i
    return item,list.count(item)
print(mostCommonItem(myList))
print(mostCommonItem(list(myTuple)))
print(mostCommonItem(list(myDictionary.values())))