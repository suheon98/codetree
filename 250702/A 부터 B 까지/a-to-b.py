a, b = map(int, input().split())
steps = []

while a <= b:
    steps.append(a)
    if a % 2 != 0:  # 홀수
        a *= 2
    else:           # 짝수
        a += 3

print(' '.join(map(str, steps)))

