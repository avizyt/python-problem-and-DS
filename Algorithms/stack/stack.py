import collections as c 

arr = [1,2,3,4,5]

stk = c.defaultdict()
for i in range(len(arr)-1):
    stk.add(i, arr[i])
print(stk) 

