a, b = map(int, input().split())
c = a + b

for i in range(b):
    print(f"{c}")
    c = c + b
