# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 2 -> Strings to Integers
######################################


def convert_add(str_list):
    sumInt = 0
    for x in str_list:
        if x.isdigit():
            sumInt += int(x)
        else:
            continue
    return sumInt


def check_duplicates(myList):
    myList2 = []
    for item in myList:
        if item not in myList2:
            myList2.append(item)
        else:
            print(item)

    if len(myList) == len(myList2):
        print("No Duplicates!")


if __name__ == '__main__':
    print(convert_add(['1', '3', '6', 'a']))
    check_duplicates(['apple', 'banana', 'watermelon', 'apple', 'watermelon'])
