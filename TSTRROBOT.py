for testcase in range(int(input())):
    # n - number of commands
    # x - initial coordinate
    # s - the input string with robot movement directions
    n, x = map(int, input().split())
    s = input()

    # The approach is to traverse the whole string and move the robot as directed while
    # recording the maximum and the minimum coordinates he has travelled to. Finally,
    # we just have to find the number of coordinates between the maximum and minimum
    # coordinates and that is our answer.
    maxi = mini = x

    for char in s:
        if char == 'L':
            x -= 1
        else:
            x += 1
        if x > maxi:
            maxi = x
        elif x < mini:
            mini = x

    res = maxi - mini + 1
    print(res)

