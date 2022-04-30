for testcase in range(int(input())):
    # n - length of the track
    # k - the maximum distance he can run
    n, k = map(int, input().split())
    # gpm - girls per kilometre
    gpm = list(map(int, input().split()))

    # Approach: We find all the possible combinations' sum of the size k in the array
    # gpm and then find the max out of all of them. That is our result.
    res = 0
    res_arr = []
    for i in range(n - k + 1):
        for j in range(k):
            res += gpm[i + j]
        res_arr.append(res)
        res = 0

    print(max(res_arr))

