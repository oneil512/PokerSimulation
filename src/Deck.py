import random

class Deck():
    def __init__(self):
        self.hearts = ['H_' + str(i) for i in list(range(1,11)) + ['J', 'Q', 'K']]
        self.spades = ['S_' + str(i) for i in list(range(1,11)) + ['J', 'Q', 'K']]
        self.clubs = ['C_' + str(i) for i in list(range(1,11)) + ['J', 'Q', 'K']]
        self.dimonds = ['D_' + str(i) for i in list(range(1,11)) + ['J', 'Q', 'K']]

        self.cards = self.hearts + self.spades + self.clubs + self.dimonds

    def shuffle(self):
        random.shuffle(self.cards)