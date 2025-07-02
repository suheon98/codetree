a = int(input())
b=0
for i in range (1, a):
    if b>=a:
        b=i-1
        break
    else:
        b=b+i
        continue 

print(b)