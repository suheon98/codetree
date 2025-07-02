import math

start, end = map(int, input().split())
cnt = 0

# 1부터 sqrt(end)까지의 소수만 검사
for i in range(2, int(math.sqrt(end)) + 1):
    square = i * i
    if square < start or square > end:
        continue
    # i가 소수인지 확인
    is_prime = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        cnt += 1

print(cnt)
