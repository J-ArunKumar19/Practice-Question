n=int(input())
arr=list(map(int,input().split()))
temp={}
if n==1:
    print(arr[0])
else:
    for i in arr:
        if i not in temp:
            temp[i]=1
        else:
            temp[i]+=1
    x=sorted(temp.items(),key=lambda x:x[1],reverse=True)
    if x[0][1]==x[1][1]:
        print(-1)
    else:
        print(x[0][0])