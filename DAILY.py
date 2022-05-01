# x - number of friends
# n - number of cars
x, n = map(int, input().split())

res = 0


def factorial(n):
    """
    :param n: a whole number
    :return: n!
    """
    fact = 1
    if n == 0:
        return fact
    else:
        for i in range(1, n+1):
            fact *= i
    return fact


def combinations(n, r):
    """
    :param n: a natural number
    :param r: a whole number
    :return: nCr
    """
    return factorial(n)//(factorial(r)*factorial(n-r))


# Approach - We take the input string containing seat allocation status and then form substrings
# from that string which represent one compartment of the car. Then, we find whether the total
# number of free seats is greater than or equal to the number of friends. If the above statement is
# true, then we find the total number of ways that these seats can be booked. We add this number to
# our result variable. After doing the above operation on each compartment of each car, we have our
# answer in the result variable.
for _ in range(n):
    s = input()
    temp = 54
    # Splitting the string for each compartment
    for i in range(0, 36, 4):
        # Forming the substring for each compartment and then
        # calculating the number of free seats
        free_places = (s[i:i+4] + s[temp-2:temp]).count('0')
        if free_places >= x:
            # Finding the total number of ways in which the free seats can be booked
            res += combinations(free_places, x)
        temp -= 2
# Printing the result
print(res)
