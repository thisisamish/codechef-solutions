for testcase in range(int(input())):
    # n - number of weird friends
    n = int(input())
    days = list(map(int, input().split()))

    # Approach: We just have to find the number of unique items in the list days.
    # That is our result. This is because Devu can give party to only one friend
    # on the same day.
    res = len(set(days))
    print(res)
