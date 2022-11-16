import deck

class Player:

    def __init__(self, name):
        self.name = name
        self.all_cards = []

    # Remove and Add cards

    def remove_one(self):
        return self.all_cards.pop(0)
    # We are removing from the top of the deck , bcs this is how it works
    # in real life when we play the game!

    def add_cards(self, new_cards):
        if type(new_cards) == type([]):
            # List of multiple Card objects
            self.all_cards.extend(new_cards)
        else:
            # For a single Card object
            self.all_cards.append(new_cards)

    # So we are adding to the deck of the player
    # if the new_cards is list , or it has more than 1 card
    # we say .extend to extend the current list with the new list
    # which in our case is new_cards
    # And else we just use .append to append a new Card object
    # which is singular to the list of cards or to the deck!

    def __str__(self):
        return f'Player {self.name} has {len(self.all_cards)} cards.'


