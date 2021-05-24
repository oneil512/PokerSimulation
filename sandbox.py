from src.Player import *
from src.utils import *

player = Player()

table_cards_three = ['H_2', 'D_4', 'C_1']
player.hand = ['H_5', 'H_6']
print(player.calc_pair_prob(table_cards_three))