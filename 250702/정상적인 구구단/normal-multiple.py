a = int(input())

for i in range(1, a + 1):
    for j in range(1, a + 1):
        if j == a:
            print(f"{i} * {j} = {i*j}", end="")  # 마지막 항에는 , 생략
        else:
            print(f"{i} * {j} = {i*j}", end=", ")
    print()