hour, minute = input().split(':')
hour = int(hour)
minute = int(minute)

# 시간 +1
hour += 1

# 출력 (분도 그대로)
print(f"{hour}:{minute}")
