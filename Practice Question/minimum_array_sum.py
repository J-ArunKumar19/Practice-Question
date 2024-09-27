N=int(input())
A=list(map(int,input().split()))
for i in range(N):
    for j in range(i+1,N):
        avg=(A[i]+A[j])/2
        if A[i]<avg:
            A[i]=0
        if A[j]<avg:
            A[j]=0
m=sum(A)
print(m)