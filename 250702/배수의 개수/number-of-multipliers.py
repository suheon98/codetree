inputs = []
for _ in range(10):
    num = int(input())
    inputs.append(num)

total_a = 0
total_b = 0

for i in inputs:
    if i % 3 == 0:
        total_a +=1
    if i % 5 == 0:
        total_b +=1

print(total_a, total_b)
