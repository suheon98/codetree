# 첫 번째 3x3 배열 입력
a = [list(map(int, input().split())) for _ in range(3)]

# 두 번째 3x3 배열 입력
b = [list(map(int, input().split())) for _ in range(3)]

# 결과 배열 생성
for i in range(3):
    row = []
    for j in range(3):
        row.append(a[i][j] * b[i][j])
    print(' '.join(map(str, row)))
