for testcase in range(int(input())):
    # n - the array length
    # k - number of elements to be inserted
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))

    # Approach: Since k is always less than n, thus the median will
    # always be from the initial array (arr before adding elements to it).
    # So we find the median index (by using the length of the final array)
    # and simply find the element at that index in the sorted initial array.
    # That is our answer.
    arr.sort()
    median_index = (n + k) // 2
    res = arr[median_index]
    print(res)
