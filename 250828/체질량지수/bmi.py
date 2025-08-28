a, b = map(int, input().split())

c= (10000*b)//(a*a)
if c>25:
    print(c)
    print("Obesity")
else:
    print(c)