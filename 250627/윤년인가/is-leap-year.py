a = int(input())

if (a % 4 == 0) and ((a % 100 != 0) or (a % 400 == 0)):
    print("true")   # 윤년
else:
    print("false")  # 윤년 아님
