import unittest
from  src.Player import Player
from src.utils import *

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.player = Player()

        self.table_cards_pair = ['H_1', 'D_1', 'D_13']
        self.table_cards_three = ['H_1', 'D_1', 'C_1']
        self.table_cards_no_pair = ['H_2', 'D_3', 'C_1']
        self.player.hand = ['H_5', 'H_6']



    def test_pair(self):
        print(getCardNum(self.player.check_pair(self.table_cards_three)))
        self.assertTrue(self.player.check_pair(self.table_cards_no_pair) == [])
        self.assertTrue(getCardNum(self.player.check_pair(self.table_cards_three)[0]) == '1')
        self.assertTrue(self.player.check_pair(self.table_cards_pair) == ['H_1', 'D_1'])

if __name__ == '__main__':
    unittest.main()
