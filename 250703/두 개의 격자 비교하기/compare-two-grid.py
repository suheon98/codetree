a = [list(map(int, input().split())) for _ in range(3)]
b = [list(map(int, input().split())) for _ in range(3)]

c = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(a[i][j] * b[i][j])
    c.append(row)

for row in c:
    print(' '.join(map(str, row)))
