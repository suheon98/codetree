import math

start, end = map(int, input().split())
cnt = 0

for i in range(start, end + 1):
    root = round(math.sqrt(i))  # 반올림 후 정수 비교
    if root * root == i:
        cnt += 1

print(cnt)
