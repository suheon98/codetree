a,b = map(int, input().split())

if a<b:
    if a==b:
        print("1 1")
    else:
        print("1 0")
else:
    if a==b:
        print("0 1")
    else:
        print("0 0")