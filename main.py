from src.Poker import Poker

def betting_round(table):
    for player in table.players:
        if not player.fold:
            # returns -1 if fold and sets fold flag
            bet = player.decide()
            if bet < 0:
                player.fold = True
                continue
            table.pot += bet

table = Poker(2)

table.deal()
betting_round(table)

table.flop()
betting_round(table)

table.turn()
betting_round(table)

table.river()
table.end_hand()