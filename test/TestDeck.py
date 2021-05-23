import unittest
from  src.Deck import Deck

class TestDeck(unittest.TestCase):
    def setUp(self):
        self.deck = Deck()
    def testcards(self):
        self.assertTrue(len(self.deck.cards) == 52)

if __name__ == '__main__':
    unittest.main()
