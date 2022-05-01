import string

for _ in range(int(input())):
    s = [char for char in input()]
    alphabets = list(string.ascii_lowercase)

    def my_ord(c):
        return alphabets.index(c) + 1

    def power(s):
        pow = 0
        for i in range(1, len(s)+1):
            pow += i * my_ord(s[i-1])
        return pow

    # Approach - We just have to sort the string array
    # to get the combination with the maximum power.
    s.sort()
    max_pow = power(s)
    print(max_pow)


