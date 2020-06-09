#map
length=map(len,['risla','zab','resmina'])
print(list(length))

#reduce
from functools import reduce
sum=reduce(lambda a,x:a+x,[2,4,5,6,7,8])
print(sum)

#filter
arr=[2,4,5,7,8,9,10]
for i in filter(lambda x:x>6,arr):
    print(i)