from src.Player import *
from src.utils import *

player = Player()

table_cards_three = ['H_1', 'D_1', 'C_1']
player.hand = ['H_5', 'H_6']
print(getCardNum(player.check_pair(table_cards_three)))