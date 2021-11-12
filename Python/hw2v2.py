import math

if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        the_max = max(a)

        new_list = []
        for j in range(the_max):
            new_list.append(0)

        # print(a)

        # print("max: " + str(the_max))

        for number in a:
            # print("number == " + str(number) + ", new_list[number] == " + str(new_list[number]))
            new_list[number - 1] += 1

        # print("new_list == " + str(new_list))

        counter = 0
        for j in range(the_max):
            counter += ((1 + new_list[j]) * new_list[j]) / 2

        counter = math.trunc(counter)
        # print("ans: " + str(counter))
        print(str(counter))
