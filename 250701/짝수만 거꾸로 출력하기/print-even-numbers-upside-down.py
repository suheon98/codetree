N = int(input())  # 입력 개수
numbers = list(map(int, input().split()))  # N개의 정수 리스트로 받기

# 역순으로 돌면서 짝수만 출력
for num in reversed(numbers):
    if num % 2 == 0:
        print(num, end=' ')
