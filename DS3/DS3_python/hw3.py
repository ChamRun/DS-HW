if __name__ == '__main__':
    n = int(input())

    for i in range(n):
        data = input()
        data = data.replace(',', '')
        pre_numbers = [int(x) for x in data.split()[1:]]
        print(pre_numbers)

        line_len = 0
        j = 0

        try:
            while j < len(pre_numbers):

                for k in range(7 - 2 ** line_len):
                    print(" ", end='')

                for k in range(2 ** line_len):
                    print(str(pre_numbers[j + k]) + " ", end='')

                print()
                j += 2 ** line_len
                line_len += 1

        except IndexError:
            print('\nDone')

        fxy = 0
        for num in pre_numbers:
            fxy += num

        print('fxy: ' + str(fxy))

        data = input()
        data = data.replace(',', '')
        past_numbers = [int(x) for x in data.split()[1:]]
        print(past_numbers)
        for num in pre_numbers:
            fxy += num

        print('fxy: ' + str(fxy))
