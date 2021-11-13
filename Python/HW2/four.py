
A = [int(x) for x in input().split()]
B = [int(x) for x in input().split()]
k = int(input())

i = 0
j = 0
kth_element = 0

while i + j != k:
    if A[i] < B[j]:
        kth_element = A[i]
        i += 1
    else:
        kth_element = B[j]
        j += 1

print("Kth element is: " + str(kth_element))

