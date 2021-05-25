from src.utils import *
from src.Deck import Deck

class Player():
    def __init__(self):
        self.hand: list = None
        self.folded = False
        self.deck_set = set(Deck().cards)

    def decide(self, table_cards):
        hand_stats = self.calculate_hand_stats(table_cards)


    def fold(self):
        pass

    def bet(self):
        pass

    def calculate_hand_stats(self, table_cards):
        pairs = self.check_pair(table_cards)
        if len(pairs) == 0:
            p = self.calc_pair_prob(table_cards)
        else:
            two_pairs = self.check_two_pair(table_cards)
            if len(two_pairs) == 0:
                tp = self.calc_two_pair_prob(table_cards)

        pairs = self.check_three_kind(table_cards)
        if len(pairs) == 0:
            p = self.calc_three_kind_prob(table_cards)
        #tk = self.calc_three_kind()
        #s = self.calc_straight()
        #f = self.calc_flush()
        #fh = self.calc_full_house()
        #fk = self.calc_four_kind()
        #sf = self.calc_straight_flush()

    def check_pair(self, table_cards) -> list:
        top_pair = []
        for i,j in crossPairListNoIdentity(table_cards + self.hand):
            if getCardNum(i) == getCardNum(j):
                if len(top_pair) > 0:
                    if getCardNum(top_pair[0]) < getCardNum(i) or getCardNum(i) == '1':
                        top_pair = [i,j]
                else:
                    top_pair = [i,j]
                        
        return top_pair

    # dict of pair possibilities and their probs
    def calc_pair_prob(self, table_cards) -> dict:
        cards = table_cards + self.hand
        remaining_deck = list(self.deck_set - self.deck_set.intersection(cards))
        probs = {}
        for i in cards:
            i_counts = 0
            num = getCardNum(i)
            for j in remaining_deck:
                # pair criterion (abstract away criterions?)
                if getCardNum(j) == num:
                    i_counts += 1
            probs[i] = i_counts / len(remaining_deck)
        return probs
        
    def check_two_pair(self, table_cards):
        pairs = []
        for i,j in crossPairListNoIdentity(table_cards + self.hand):        
            if getCardNum(i) == getCardNum(j):
                pairs.append([i,j])
                        
        if len(pairs) == 2:
            return pairs
        return []

    # dict of pair possibilities and their probs
    # we will only ever get here if we have one pair already
    def calc_two_pair_prob(self, table_cards) -> dict:
        cards = table_cards + self.hand
        remaining_deck = list(self.deck_set - self.deck_set.intersection(cards))
        probs = {}

        for i,j in crossPairListNoIdentity(cards):
            if getCardNum(i) == getCardNum(j):
                del cards[cards.index(i)]
                del cards[cards.index(j)]

        for i in cards:
            i_counts = 0
            num = getCardNum(i)
            for j in remaining_deck:
                # pair criterion (abstract away criterions?)
                if getCardNum(j) == num:
                    i_counts += 1
            probs[i] = i_counts / len(remaining_deck)
        return probs

    def check_three_kind(self, table_cards) -> list:
        top_trio = []
        cards = table_cards + self.hand
        for i_, i in enumerate(cards):
            for j_, j in enumerate(cards[(i_ + 1):]):
                for k in cards[(i_ + j_ + 2):]: 
                    if getCardNum(i) == getCardNum(j) and getCardNum(i) == getCardNum(k) and getCardNum(j) == getCardNum(k):
                        if len(top_trio) > 0:
                            if getCardNum(top_trio[0]) < getCardNum(i) or getCardNum(i) == '1':
                                top_trio = [i,j,k]
                        else:
                            top_trio = [i,j,k]
                        
        return top_trio