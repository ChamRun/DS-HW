import math

numbers = [int(x) for x in input().split()]
n = len(numbers)

counting_list = []
sorted_list = []

for i in range(n):
    counting_list.append(0)
    sorted_list.append(0)

# 1st counting sort: based on "a2"

for number in numbers:
    a2 = number % n
    counting_list[a2] += 1

for i in range(1, n):
    counting_list[i] += counting_list[i - 1]

for i in range(n - 1, -1, -1):
    a2 = numbers[i] % n
    sorted_list[counting_list[a2] - 1] = numbers[i]
    counting_list[a2] -= 1

for i in range(n):
    numbers[i] = sorted_list[i]

# 2nd counting sort: based on a1

for i in range(n):
    counting_list[i] = 0
    sorted_list[i] = 0

for number in numbers:
    a1 = (math.trunc(number / n)) % n
    counting_list[a1] += 1

for i in range(1, n):
    counting_list[i] += counting_list[i - 1]

for i in range(n - 1, -1, -1):
    a1 = (math.trunc(numbers[i] / n) % n)
    sorted_list[counting_list[a1] - 1] = numbers[i]
    counting_list[a1] -= 1

numbers = sorted_list
print(numbers)
