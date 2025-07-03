a, b = map(int, input().split())
list_a = []
list_b = []
list_c = []

# 첫 번째 배열 입력 (a줄, 각 줄에 b개 정수)
for _ in range(a):
    row = list(map(int, input().split()))
    list_a.append(row)

# 두 번째 배열 입력
for _ in range(a):
    row = list(map(int, input().split()))
    list_b.append(row)

# 결과 비교 후 list_c 구성
for i in range(a):
    row = []
    for j in range(b):
        if list_a[i][j] == list_b[i][j]:
            row.append(0)
        else:
            row.append(1)
    list_c.append(row)

# 결과 출력
for row in list_c:
    print(' '.join(map(str, row)))
