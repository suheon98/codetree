arr = list(map(int, input().split()))

for i in range(0, 8):
    arr.append((arr[i] + arr[i+1])%10)

print(' '.join(map(str, arr)))