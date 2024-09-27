import math
from collections import Counter
def prime(num):
    factor=[]
    while num%2==0:
        factor.append(2)
        num//=2
    for i in range(3,int(math.sqrt(num))+1,2):
        while num%i==0:
            factor.append(i)
            num//=i
    if num>2:
        factor.append(num)
    return Counter(factor)
def Calculate(arr,num):
    if not arr:
        return -1
    fc=prime(num)
    total=0
    n=len(arr)
    for p,exponent in fc.items():
        if p<n:
            total+=exponent*arr[p]
        else:
            return 0
    return total
n=int(input())
arr=list(map(int,input().split()))
num=int(input())
result=Calculate(arr,num)
print(result)