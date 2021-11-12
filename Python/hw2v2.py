if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n = int(input())
        a = [int(x) for x in input().split()]
        the_max = max(a)

        new_list = []
        for j in range(the_max + 1):
            new_list.append(0)

        print(a)

        print("max: " + str(the_max))

        for number in a:
            # print("number == " + str(number) + ", new_list[number] == " + str(new_list[number]))
            new_list[number] += 1

        print("new_list == " + new_list)
