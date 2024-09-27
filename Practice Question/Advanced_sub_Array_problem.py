goals = int(input())
size = int(input())
l = list(map(int, input().split()))
if size > len(l):
    print("Error: size is greater than the length of the list")
else:
    mx = 0
    for i in range(0, len(l)):
        sub = l[i:i+size]
        k = 1
        s = 0
        for j in sub:
            s += (j*k)
            k += 1
            if s > mx:
                mx = s
    print(mx)