import player
import deck


class Computer:

    def __init__(self, deck_of_cards):
        self.all_cards = deck_of_cards.all_cards_func()
        self.amount = 9999999

    def pot(self, amount):
        if player.check_if_valid_amount(amount, range(1, 99999999)):
            self.amount += amount

    def hit(self):
        return self.all_cards.pop(0)

