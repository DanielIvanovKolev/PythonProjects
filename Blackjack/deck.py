import random
import card


class Deck:

    def __init__(self):

        self.all_cards = []

        # Creating two decks of cards ,bcs is blackjack and there are more than 1 deck
        for x in range(2):
            for suit in card.suits:
                for rank in card.ranks:
                    # Create the Card Object
                    created_cards = card.Card(suit, rank)

                    self.all_cards.append(created_cards)

    def shuffle(self):
        random.shuffle(self.all_cards)

    def deal_one(self):
        return self.all_cards.pop(0)

    def all_cards_func(self):
        return self.all_cards



