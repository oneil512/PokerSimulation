from src.utils import *

class Player():
    def __init__(self):
        self.hand: list = None
        self.folded = False

    def decide(self, table_cards):
        # logic
        hand_probabilities = self.calculate_hand_probabilities(table_cards)
        self.fold()
        self.bet()

    def fold(self):
        pass

    def bet(self):
        pass

    def calculate_hand_probabilities(self, table_cards):
        pairs = self.check_pair(table_cards)
        if len(pairs) == 0:
            p = self.calc_pair(table_cards)

        #tp = self.calc_two_pair()
        #tk = self.calc_three_kind()
        #s = self.calc_straight()
        #f = self.calc_flush()
        #fh = self.calc_full_house()
        #fk = self.calc_four_kind()
        #sf = self.calc_straight_flush()

    def check_pair(self, table_cards) -> list:
        top_pair = []
        for i_, i in enumerate(table_cards + self.hand):
            for j in (table_cards + self.hand)[(i_ + 1):]:
                if getCardNum(i) == getCardNum(j):
                    if len(top_pair) > 0:
                        if getCardNum(top_pair[0]) < getCardNum(i) or getCardNum(i) == '1':
                            top_pair = [i,j]
                    else:
                        top_pair = [i,j]
                        
        return top_pair

        
    def calc_pair(self, table_cards):
        pass
