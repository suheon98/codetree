N = int(input())

for _ in range (N):
    total = 0
    a, b = map(int, input().split())
    for i in range (a, b+1):
        if i%2==0:
            total=total+i
    print(total)