# 3행 3열 배열 입력 받기
matrix = []
for _ in range(3):
    row = list(map(int, input().split()))
    matrix.append(row)

# 3배 만들기
for i in range(3):
    for j in range(3):
        matrix[i][j] *= 3

# 출력
for row in matrix:
    print(' '.join(map(str, row)))
