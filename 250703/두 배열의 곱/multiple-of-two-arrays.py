# N, M 입력
N, M = map(int, input().split())

# 첫 번째 격자 입력
a = [list(map(int, input().split())) for _ in range(N)]

# 두 번째 격자 입력
b = [list(map(int, input().split())) for _ in range(N)]

# 결과 배열 생성
for i in range(N):
    row = []
    for j in range(M):
        if a[i][j] == b[i][j]:
            row.append(0)
        else:
            row.append(1)
    print(' '.join(map(str, row)))
