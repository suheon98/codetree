N, M = map(int, input().split())

a = [list(map(int, input().split())) for _ in range(N)]
b = [list(map(int, input().split())) for _ in range(N)]

result = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(0 if a[i][j] == b[i][j] else 1)
    result.append(row)

for row in result:
    print(' '.join(map(str, row)))
