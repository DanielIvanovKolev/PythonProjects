# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 1 -> Division and Square Root
######################################
from math import sqrt


def divide_or_square(number):
    if number % 5 == 0:
        return sqrt(number)
    else:
        return number % 5


# first_element = list(dict.values())[0]  # Taking the first element of a dictionary


# We use the max function to return the max value of the dictionary
# values. The max function has a key parameter. Since we are looking for the first
# longest value, we pass len to the key parameter. If we do not pass len to the key
# parameter, it will return green as the longest value which is lexicographically larger
# than apple.
def longest_value(d: dict):
    # Using max and key len to get the longest value
    longest = max(d.values(), key=len)
    # key=len -> For example with a list of strings, specifying key=len (the built in len() function)
    # sorts the strings by length, from shortest to longest.
    # The sort calls len() for each string to get the list of proxy length values,
    # and then sorts with those proxy values.
    # And with the max() function we take the longest value that the key=len returns.
    return longest


if __name__ == '__main__':
    print(str(round(divide_or_square(10), 2)))  # Round it up to the second decimal
    print(longest_value({'fruits': 'apples', 'color': 'green'}))
