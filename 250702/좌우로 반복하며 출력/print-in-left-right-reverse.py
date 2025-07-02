N = int(input())

for i in range(N):
    if i % 2 == 0:  # 짝수 줄 (0, 2, ...)
        for j in range(1, N+1):
            print(j, end="")
    else:           # 홀수 줄 (1, 3, ...)
        for j in range(N, 0, -1):
            print(j, end="")
    print()  # 줄 바꿈
