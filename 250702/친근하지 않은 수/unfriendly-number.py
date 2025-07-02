a = int(input())
b=0
for i in range (1, a):
    if i % 2==0 or i % 3 == 0 or i % 5 == 0:
        continue
    else:
        b+=1

print(b)