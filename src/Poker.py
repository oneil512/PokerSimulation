from src.Deck import Deck
from src.Player import Player

class Poker():
    def __init__(self, players: int):
        self.bigBlind: int = 2
        self.bigBlind: int = int(self.bigBlind // 2)
        self.deck = Deck()
        self.players = []
        self.tableCards = []
        self.pot = 0
        for _ in range(players):
            self.players.append(Player())

    def deal(self):
        self.deck.shuffle()
        for player in self.players:
            player.hand.append(self.deck.pop())
            player.hand.append(self.deck.pop())


    def flop(self):
        self.tableCards.append(self.deck.pop())
        self.tableCards.append(self.deck.pop())
        self.tableCards.append(self.deck.pop())

    def turn(self):
        self.tableCards.append(self.deck.pop())

    def river(self):
        self.tableCards.append(self.deck.pop())

    def end_hand(self):
        self.deck = Deck()
        self.tableCards = []
        self.pot = 0

        for player in range(self.players):
            player.hand = []
            player.fold = False

        winners = self.determine_winners()
        self.pay_winners(winners)

    # returns dict of players and amounts they win
    def determine_winners(self) -> dict:
        return {}

    def pay_winners(winners: dict):
        for player, payout in winners.items():
            player.cash += payout
