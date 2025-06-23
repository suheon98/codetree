a,b = map(int, input().split())

if a>b:
    c=a*b
    print(f"{c}")
else:
    c=b/a
    print(f"{int(c)}")