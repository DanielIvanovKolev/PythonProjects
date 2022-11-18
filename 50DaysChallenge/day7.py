# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 7 -> A String Range
######################################

def string_range(num):
    str_list = [str(i) for i in range(num)]
    return '.'.join(str_list)


def dict_of_names(names: list):
    my_dict = {}
    for item in names:
        if item[0].capitalize() == 'S':
            # We can also use item.startswith(S)
            if item in my_dict:
                my_dict[item] += 1
            else:
                my_dict[item] = 1
            # Dictionary update method
            # my_dict.update({item: names.count(item)})
            # We can also use COUNTER
            # count = []
            # if item.startswith('S"):
            #   count.append(item)
            # names = Counter(count)
            # The counter class from collections module keeps
            # track of elements and their count and stores the result
            # in a dictionary.
            # It returns the name of the element as the key and its count
            # as the value
    return my_dict


names_list = ['Sasha', 'Sofia', 'Gloria', 'Matilda', 'Simeone', 'Sasha', 'Simeone']
if __name__ == '__main__':
    print(string_range(20))
    print(dict_of_names(names_list))
