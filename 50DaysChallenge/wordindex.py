# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 4 -> Only Floats
######################################

def only_floats(a, b):
    if type(a) == float:
        if type(b) == float:
            return 2
        else:
            return 1
    elif type(b) == float:
        if type(a) == float:
            return 2
        else:
            return 1
    else:
        return 0


def word_index(myList):
    longest = max(myList, key=len)
    # key=len -> For example with a list of strings, specifying key=len (the built in len() function)
    # sorts the strings by length, from shortest to longest.
    # The sort calls len() for each string to get the list of proxy length values,
    # and then sorts with those proxy values.
    # And with the max() function we take the longest value that the key=len returns.
    if len(set(map(len, myList))) == 1:
        # With this we check first the len of all the items in the list using map
        # map() function works as an iterator to return a result after applying a
        # function to every item of an iterable(tuple, list, etc)
        # Then with set we see if there is only 1 unique item left
        # If there is then all the words are with the same length
        # If not then we continue to search for the index of the longest word
        return 0
    else:
        for index, item in enumerate(myList):
            if longest == item:
                return index


listStr  = ["Hate", "remorse", "vengeance"]
listStr2 = ["Love", "Hate", "Hate", "Hate", "Hate", "Hate", "Hate", "Hates"]
if __name__ == '__main__':
    print(only_floats(12, 20))
    print(word_index(listStr))
    print(word_index(listStr2))
