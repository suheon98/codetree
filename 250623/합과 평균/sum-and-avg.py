num1_input = input("첫 번째 수를 입력하세요: ")
num2_input = input("두 번째 수를 입력하세요: ")

num1 = float(num1_input)
num2 = float(num2_input)

total = num1 + num2
average = total / 2
print(f"합: {total}")
print(f"평균: {average:.2f}")
