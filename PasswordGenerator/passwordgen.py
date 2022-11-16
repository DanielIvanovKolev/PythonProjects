# Password Generator
import random
import string

# Lists of the alphabet symbols and numbers
alphabet = list(string.ascii_letters)
symbols = ['!', '@', "#", "$", '%', '^', '&', '*', '(', ')', '_', '+',
           '.', ',', ';', ':', '[', ']', '{', '}', '|', '-']
numbers = list(string.digits)

# Variable for while loop
while_password = True

while while_password:
    # Password Length
    while True:
        pass_len = input("How long would you like your password to be: ")
        if pass_len.isdigit():
            pass_len = int(pass_len)
            break
        else:
            print("Wrong Input!")
            continue

    while True:
        pass_amount = input("How many password you want to generate: ")
        if pass_amount.isdigit():
            pass_amount = int(pass_amount)
            break
        else:
            print("Wrong Input!")
            continue

    # Password Combinations

    # #.1 If the user wants to have symbols in their password
    while True:
        pass_chars = input("Do you want your password to have symbols?: (Y or N)")
        if pass_chars.capitalize().isalpha() and pass_chars == 'Y':
            print("\nGenerating symbols...\n")
            break
        elif pass_chars.capitalize().isalpha() and pass_chars == 'N':
            break
        else:
            print("Wrong Input!")
            continue

    # #.2 If the user wants to have numbers in their password
    while True:
        pass_nums = input("Do you want your password to have numbers?: (Y or N)")
        if pass_nums.capitalize().isalpha() and pass_nums == 'Y':
            print("\nGenerating numbers...\n")
            break
        elif pass_nums.capitalize().isalpha() and pass_nums == 'N':
            break
        else:
            print("Wrong Input!")
            continue

    while_generating = True

    while while_generating:
        all_password = []
        random.shuffle(alphabet)
        random.shuffle(symbols)
        random.shuffle(numbers)

        counter = 1

        symbol = False
        nums = False

        if pass_chars == 'Y':
            counter += 1
            symbol = True
            if pass_nums == 'Y':
                counter += 1
                nums = True
            else:
                pass
        elif pass_nums == 'Y':
            counter += 1
            nums = True
        else:
            pass

        for y in range(pass_amount):
            user_password = []
            for x in range(pass_len):
                random_num_alphabet = 0
                random_num_symbols  = 0
                random_num_numbers  = 0

                if counter == 1:
                    random_num_alphabet = random.randint(0, len(alphabet) - 1)
                elif counter == 2 and symbol is True:
                    random_num_alphabet = random.randint(0, len(alphabet) - 1)
                    random_num_symbols  = random.randint(0, len(symbols) - 1)
                elif counter == 2 and nums is True:
                    random_num_alphabet = random.randint(0, len(alphabet) - 1)
                    random_num_numbers  = random.randint(0, len(numbers) - 1)
                elif counter == 3:
                    random_num_alphabet = random.randint(0, len(alphabet) - 1)
                    random_num_symbols  = random.randint(0, len(symbols) - 1)
                    random_num_numbers  = random.randint(0, len(numbers) - 1)

                random_num = random.randint(1, counter)

                if random_num == 1:
                    user_password.append(alphabet[random_num_alphabet])
                elif random_num == 2 and symbol is True:
                    user_password.append(symbols[random_num_symbols])
                elif random_num == 2 and nums is True:
                    user_password.append(numbers[random_num_numbers])
                elif random_num == 3:
                    user_password.append(numbers[random_num_numbers])
                else:
                    print("Something is wrong!")

            all_password.append(''.join(user_password))

        print("\n")
        for value in all_password:
            print(value)

        while True:
            new_pass = input("\nDo you want a new generation of the same passwords "
                             "or you want a brand new passwords?: \n"
                             "YN - for new generation\n"
                             "YBN - for brand new passwords\n"
                             "N - exiting\n"
                             "Answer: ")
            if new_pass.capitalize().isalpha() and new_pass == 'N':
                print("\nExiting...\n")
                while_generating = False
                while_password = False
                break
            elif new_pass.capitalize().isalpha() and new_pass == 'YN':
                break
            elif new_pass.capitalize().isalpha() and new_pass == 'YBN':
                while_generating = False
                break
            else:
                print("Wrong Input!")
                continue
