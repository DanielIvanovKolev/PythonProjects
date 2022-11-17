# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 5 -> My Discount
######################################

def my_discount():
    while True:
        price = input("What is the price of the product?: ")
        if price.isdigit():
            price = int(price)
            break
        else:
            continue

    while True:
        discount = input("What percentage is the discount?: ")
        if discount.isdigit():
            discount = int(discount)
            break
        else:
            continue

    return price - (price*(discount/100))


def studentGender(gender: list):
    temp_list = []
    list_male = []
    list_female = []

    for item in gender:
        if item.lower() == 'male':
            list_male.append(item.lower())
        elif item.lower() == 'female':
            list_female.append(item.lower())
        else:
            continue

    temp_list.append((list_male[0].capitalize(), list_male.count('male')))
    temp_list.append((list_female[0].capitalize(), list_female.count('female')))

    return temp_list


students = ['Male', 'female', 'Female', 'male',
            'male', 'male', 'Female', 'Male',
            'female', 'female', 'Female']
if __name__ == '__main__':
    print(my_discount())
    print(studentGender(students))
