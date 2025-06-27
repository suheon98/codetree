a1 = int(input())
a2 = int(input())

if a1 == 0:
    if a2 >= 19:
        print("MAN")
    else:
        print("BOY")
else:
    if a2 >= 19:
        print("WOMAN")
    else:
        print("GIRL")