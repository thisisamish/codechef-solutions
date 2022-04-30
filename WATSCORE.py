for testcase in range(int(input())):
    # n - number of submissions
    n = int(input())

    # Approach: Start storing all the submissions of problems numbered till 8 (since 8-11 problems are non-scorable)
    # in a dictionary as problem_num: score. Then we keep updating the dictionary if we find a higher score
    # for an already stored problem number. Finally, we sum all the values of this dictionary and that is
    # our result.
    sub_dict = {}
    for i in range(n):
        p, s = map(int, input().split())
        if p <= 8:
            if p in sub_dict.keys():
                sub_dict[p] = max(sub_dict[p], s)
            else:
                sub_dict[p] = s
        else:
            continue
    res = sum(sub_dict.values())
    print(res)
