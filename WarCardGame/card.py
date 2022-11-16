"""
This is a card class for the war Game
Here we're just checking if the user input is correct
and if there is a such a card in the deck!
"""

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')

values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8,
          'Nine': 9, 'Ten': 10, 'Jack': 11, 'Queen': 12, 'King': 13, 'Ace': 14}


class Card:

    def __init__(self, suit, rank):
        self.suit = suit.capitalize()
        self.rank = rank.capitalize()
        self.value = values[rank.capitalize()]

    def __str__(self):
        return self.rank + " of " + self.suit

    def check_if_there(self):
        flag = False
        if self.suit in suits and self.rank in ranks:
            flag = True

        return flag


#two_hearts = Card("Spades", "King")
#three_of_clubs = Card("Clubs", "king")

#if two_hearts.check_if_there():
#    print(two_hearts)
#else:
#    print("This is not correct! There is not a suit called {}".format(two_hearts.suit))
