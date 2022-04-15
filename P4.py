n = int(input())
array = map(int,input().split())
maximum = max(array)
i = array.count(maximum)
for j in range(i):
    array.remove(maximum)
print(max(array))