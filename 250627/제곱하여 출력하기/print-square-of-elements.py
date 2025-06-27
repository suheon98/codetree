N = int(input())                           # 첫 줄: 개수 입력
arr = list(map(int, input().split()))     # 두 번째 줄: N개의 정수 입력

for num in arr:
    print(num ** 2, end=' ')              # 각 수의 제곱을 공백으로 출력
