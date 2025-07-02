# 2차원 배열 입력 받기
matrix = []

for _ in range(4):
    row = list(map(int, input().split()))  # 한 줄에 4개의 정수 입력
    matrix.append(row)

# 각 줄(행)의 합 출력
for row in matrix:
    print(sum(row))
