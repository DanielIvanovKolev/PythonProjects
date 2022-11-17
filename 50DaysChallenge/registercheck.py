# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 3 -> Register Check
######################################

def register_check(d: dict):
    count = 0
    for value in d.values():
        if value == 'yes':
            count += 1
        else:
            continue
    return count


def lower_case(myList):
    tupleNames = []
    for item in sorted(myList, reverse=True):
        # We use sorted to sort the list in desc order!!!
        if item.islower():
            tupleNames.append(item)
        else:
            continue
    tupleNames = tuple(tupleNames)
    return tupleNames


names = ["kerry", "John", "Mary", "carol", "Rose", "adam", "dickson"]
register = {'Michael': 'yes', 'John': 'yes', 'Peter': 'yes', 'Daniel': 'yes'}
if __name__ == '__main__':
    print(register_check(register))
    print(lower_case(names))