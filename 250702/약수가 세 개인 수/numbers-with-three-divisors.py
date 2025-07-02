import math

start, end = map(int, input().split())
cnt = 0

for i in range(start, end + 1):
    root = math.isqrt(i)  # 정확한 정수 제곱근
    if root * root == i:
        cnt += 1

print(cnt)
