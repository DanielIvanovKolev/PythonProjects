# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 6 -> User Name Generator
######################################

def user_name(email):
    temp_list = []
    for x in range(0, len(email)):
        if email[x] == '@' and (email[x + 1] == 'g' or email[x + 1] == 'a'):
            break
        else:
            temp_list.append(email[x])

    return ''.join(temp_list)


def zeroed(num: list):
    num.pop(0)
    num.pop(-1)

    num.insert(0, 0)
    num.insert(len(num), 0)

    return num


num_list = [2, 5, 7, 8, 9]
if __name__ == '__main__':
    print(user_name("jorji_8@@@@@9222JO@!jos#4@gmail.com"))
    print(zeroed(num_list))
