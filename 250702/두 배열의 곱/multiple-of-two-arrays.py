# 3행 3열 배열 입력 받기
a = []
b = []

for _ in range(3):
    row = list(map(int, input().split()))
    a.append(row)

for _ in range(3):
    row = list(map(int, input().split()))
    b.append(row)

# c를 결과로 새로 구성
c = []
for i in range(3):
    row = []
    for j in range(3):
        row.append(a[i][j] * b[i][j])
    c.append(row)

# 출력
for row in c:
    print(' '.join(map(str, row)))
