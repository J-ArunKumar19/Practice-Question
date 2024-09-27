N=int(input())
A=list(map(int,input().strip().split()))[:N]
count=0
sum=0
for i in A:
    sum+=i
    if sum==0:
        count+=1
print(count)