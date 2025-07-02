words = ["apple", "banana", "grape", "blueberry", "orange"]
target = input()
count = 0

for word in words:
    if len(word) >= 4 and (word[2] == target or word[3] == target):
        print(word)
        count += 1

print(count)