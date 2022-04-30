import string

for testcase in range(int(input())):
    alphabet_arr = list(string.ascii_lowercase)  # Generating a list of lowercase alphabets
    price_arr = list(map(int, input().split()))  # Getting input about the prices of letters
    prices = dict(zip(alphabet_arr, price_arr))  # Creating a dictionary by mapping letters with their prices
    string_arr = set(input())  # Getting input string in the form of a set so as to remove duplicate letters
    replace = set(alphabet_arr) - string_arr  # Finding the letters to be replaced by subtracting already present
    # letters from all the letters. This "subtraction" syntax only works for sets.
    res = 0
    for letter in replace:
        res += prices[letter]  # Adding the prices of the letters to be removed
    print(res)  # Printing the final result




