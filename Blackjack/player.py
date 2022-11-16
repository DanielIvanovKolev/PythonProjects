"""
Class player
where we store the name and the balance of the player
He can withdraw or deposit money in his acc
When he is at 0 dollars he will lose and leave the table
"""

# Range for the money that we can deposit
money_range = range(1, 10001)
money_range_withdraw_pot = range(1, 100001)
money_range_bet = [0, 1, 5, 10, 50, 100, 500, 1000]


# Function to check if certain amount is valid
def check_if_valid_amount(amount, range_of_amount):
    if amount.isdigit():
        amount = int(amount)

        if amount in range_of_amount:
            return True
        else:
            print("\nWrong amount! You are inputting out of range value\n")
            return False

    else:
        print("\nWrong Amount! You are inputting an invalid value!\n")
        return False


class Player:

    def __init__(self):

        # Checking if the name is valid with the isaplha method
        # If it's not alphabetical then the user should try again
        # And if it is then we break from the loop
        while True:
            self.name = input("What is your name? :")

            if self.name.isalpha():
                break
            else:
                print("Invalid Name! Enter new one!\n")
                continue

        # We are checking if the user is inputting a valid amount of money
        # First we check if he is inputting a string , then if the user is in the range
        # if not then he should try again and so on until he inputs a valid amount
        while True:
            amount_money = input("How much money you want to deposit to your account? : ")

            if check_if_valid_amount(amount_money, money_range):
                self.balance = int(amount_money)
                break
            else:
                continue


    def __str__(self):
        return f'Player {self.name} has {self.balance} money in their account.'

    # This is the winning from the table

    def pot(self, amount):
        self.balance += amount

    # Withdraw any time at the game and leave the table and go home
    def withdraw(self):
        while True:
            amount = input("How much money you want withdraw/bet: ")

            if self.check_balance(amount, money_range_withdraw_pot):
                print("Successful withdraw!\n")
                break
            else:
                print("Invalid withdraw!\n")
                continue

    # Bet - The player can bet on the game if they have money
    # and in the certain range [1, 5, 10, 50, 100, 500, 1000]
    def bet(self):
        while True:
            amount = input("How much you want to bet:")

            if self.check_balance(amount, money_range_bet):
                print("Successful bet!")
                return int(amount)
            else:
                print("Unsuccessful bet!")
                continue

    def player_balance(self):
        return self.balance
        #print(f"You have {self.balance} dollars!")

    # Function for checking if the player have the amount
    # That he want to do something with!!!
    # In that function we call check_if_valid_amount
    # that checks if the amount that the player has given
    # is in the range that is given on the top of this file
    # the function works for everything: withdraw, bet, pot and deposit
    def check_balance(self, amount, range_of_amount):

        if check_if_valid_amount(amount, range_of_amount):
            if self.balance < int(amount):
                print("\nNot enough money in the account!")
                print(f"You have {self.balance} dollars!\n")
                return False
            else:
                self.balance -= int(amount)
                return True
        else:
            return False
