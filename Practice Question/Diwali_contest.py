N=int(input())
p=int(input())
time=240-p
left=time
i=1
while i<=N and 5*i<=left:
    left-=5*i
    i+=1
print(i-1)