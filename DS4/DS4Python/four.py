def find_longest_answer(array):
    n = len(array)
    dp = []

    for i in range(len(array)):
        maximum = 1

        for j in range(i):
            # print('checking ' + str(array[j]))
            if array[j] < array[i] and maximum <= dp[j]:
                # print(str(i) + ' comes after ' + str(j))
                maximum = dp[j] + 1

        dp.append(maximum)
        print(str(array[i]) + ":" + str(dp[i]))

    return max(dp)


if __name__ == '__main__':
    answer = find_longest_answer([1, 2, 4, 3, 6, 7])
    print(answer)
