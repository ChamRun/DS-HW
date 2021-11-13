

numbers = [int(x) for x in input().split()]

i = 0
for j in range(len(numbers)):
    if numbers[j] < 0:
        numbers[i], numbers[j] = numbers[j], numbers[i]
        i += 1

print(numbers)

