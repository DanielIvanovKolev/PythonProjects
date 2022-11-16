suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven',
         'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank  # 'jack'
        self.value = values[rank.capitalize()]

    def __str__(self):
        return self.rank + " of " + self.suit

    # This function is only if we have user input to the program
    # to check if there is such a card
    def check_if_there(self):
        flag = False
        if self.suit in suits and self.rank in ranks:
            flag = True

        return flag
