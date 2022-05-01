for testcase in range(int(input())):
    # n - number of songs
    n = int(input())
    lengths = list(map(int, input().split()))
    # k - position of "Uncle Johny" song
    k = int(input())

    # Approach - First, we find the index of the "Uncle Johny" song
    # in the unsorted list. Then we sort the list and find the index
    # of the "Uncle Johny" song in the sorted list. Add 1 to the index
    # and we have the answer.
    song_len = lengths[k - 1]
    lengths.sort()
    res = lengths.index(song_len) + 1
    print(res)
