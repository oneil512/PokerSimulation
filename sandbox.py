from src.Player import *
from src.utils import *

player = Player()

table_cards_three = ['S_9', 'D_9', 'C_9', 'C_1']
player.hand = ['S_1', 'H_1']
print(player.check_three_kind(table_cards_three))