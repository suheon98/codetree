matrix = []

for _ in range(4):
    row = list(map(int, input().split()))  # 한 줄에 4개의 정수 입력
    matrix.append(row)

cnt = 0
for row in matrix:
    for num in row:
        if num % 5 == 0:
            cnt += 1

print(cnt)