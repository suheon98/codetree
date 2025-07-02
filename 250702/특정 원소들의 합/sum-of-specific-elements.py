matrix = []

for _ in range(4):
    row = list(map(int, input().split()))  # 한 줄에 4개의 정수 입력
    matrix.append(row)

total = 0
for i in range (4):
    for j in range (i+1):
        total += matrix[i][j]

print(total)