dictionary1 = {1:'a',2:'b','c':'d'}
dictionary2 = {3:'f',0:'g'}
dictionary3 = {1.28:'i','j':'k',-9:'l'}
keys2 = list(dictionary2.keys())
keys3 = list(dictionary3.keys())
values2 = list(dictionary2.values())
values3 = list(dictionary3.values())
values = values2+values3
keys = keys2+keys3
for i in range(len(keys)):
        dictionary1[keys[i]] = values[i]
print(dictionary1) 