for testcase in range(int(input())):
    m, w = input().split()

    # I copied this function from GeeksForGeeks' portal.
    def is_subsequence(str1, str2):
        m = len(str1)
        n = len(str2)

        j = 0  # Index of str1
        i = 0  # Index of str2

        # Traverse both str1 and str2
        # Compare current character of str2 with
        # first unmatched character of str1
        # If matched, then move ahead in str1

        while j < m and i < n:
            if str1[j] == str2[i]:
                j = j + 1
            i = i + 1

        # If all characters of str1 matched,
        # then j is equal to m
        return j == m


    # Approach - We simply test if either the man's name is a subsequence of
    # the woman's name or vice-versa. If either is true, then print YES, otherwise
    # print NO.
    if is_subsequence(m, w) or is_subsequence(w, m):
        print("YES")
    else:
        print("NO")


# My final solution which had fault in the subseq function:

# for testcase in range(int(input())):
#     m, w = input().split()
#
#
#     def subseq(str1, str2):
#         j = 0
#         for i in range(len(str1)):
#             while j < len(str2):
#                 if str1[i] == str2[j]:
#                     j += 1
#                     break
#                 else:
#                     if j == len(str2) - 1:
#                         return "NO"
#                 j += 1
#         return "YES"
#
#
#     h1 = subseq(m, w)
#     h2 = subseq(w, m)
#
#     if h1 == "YES" or h2 == "YES":
#         print("YES")
#     else:
#         print("NO")



