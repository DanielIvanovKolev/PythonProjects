# 50 days of python. A Challenge a Day - Benjamin Bennet Alexander
######################################
# Day 8 -> Odd and Even, Prime Numbers
######################################


# With lists
def odd_even(numbers: list):
    odd_list  = []
    even_list = []

    for x in numbers:
        if x % 2 == 0:
            even_list.append(x)
        else:
            odd_list.append(x)
    return max(even_list) - max(odd_list)


# With variables
def odd_even_variable(numbers: list):
    max_odd  = 0
    max_even = 0

    for x in numbers:
        if x % 2 != 0 and max_odd < x:
            max_odd = x
        if x % 2 == 0 and max_even < x:
            max_even = x
    return max_even - max_odd


def prime_numbers(a=int(input("Number: "))):
    list_prime = []
    for i in range(2, a + 1):
        if i > 1:
            for j in range(2, i):
                if i % j == 0:
                    break
            else:
                list_prime.append(i)
                # We are using for else statement
                # so if the for loop finished normally the else statement will be
                # executed. Otherwise, it will not. So in our case we have an
                # if statement inside the for loop that checks for something
                # if the statement is correct the loop will be terminated
                # and in that case the else statement will not execute and the
                # not prime number will not be appended in the list.
                # When the number is prime the if statement will not execute
                # and the loop will finish normally so in that case the else
                # statement will execute and the number will be appended in the list.
    return list_prime


numbers_list = [6, 4, 2, 3, 1, 8, 12, 32, 43, 12, 35, 89, 28]
if __name__ == '__main__':
    print(odd_even(numbers_list))
    print(odd_even_variable(numbers_list))
    print(prime_numbers())
