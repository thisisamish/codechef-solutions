for testcase in range(int(input())):
    n = int(input())
    s = input()
    r = input()

    # Approach: Find the number of zeroes or ones in both the strings.
    # If they match then the answer is YES, otherwise NO.
    # P.S. - We only need to find either zeroes or ones because the string
    # is made up of only zeroes and ones so if one of them doesn't match,
    # the other definitely won't.

    s_ones = s.count('1')
    r_ones = r.count('1')

    if s_ones == r_ones:
        print("YES")
    else:
        print("NO")
