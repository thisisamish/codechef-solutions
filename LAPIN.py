for testcase in range(int(input())):
    string_arr = list(input())
    size = len(string_arr)

    # Splitting the string_array into two parts depending upon whether the number of items
    # (or characters, in case of the string) is even or odd.
    if size % 2 == 0:
        left_arr = string_arr[:size//2]
        right_arr = string_arr[size//2:]
    else:
        left_arr = string_arr[:size//2]
        right_arr = string_arr[size//2 + 1:]

    # Sorting the two arrays
    left_arr.sort()
    right_arr.sort()

    # Checking if the left array is equal to the right array or not, after sorting.
    # This basically implements the logic of the problem - to check whether we have
    # the same characters with the same frequency on both sides or not.
    if left_arr == right_arr:
        print("YES")
    else:
        print("NO")
