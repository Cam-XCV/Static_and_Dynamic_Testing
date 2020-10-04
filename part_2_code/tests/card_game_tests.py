import unittest
from src.card import Card
from src.card_game import CardGame

class TestCardGame(unittest.TestCase):
    
    def setUp(self):
        self.card1 = Card("Hearts", 10)
        self.card2 = Card("Clubs", 1)
        self.cards = [self.card1, self.card2]
        self.cardgame = CardGame()


    def test_check_for_ace_false(self):
        self.assertEqual(False, self.cardgame.check_for_ace(self.card1))
    
    def test_check_for_ace_true(self):
        self.assertEqual(True, self.cardgame.check_for_ace(self.card2))

    def test_highest_card(self):
        self.assertEqual(self.card1, self.cardgame.highest_card(self.card1, self.card2))

    def test_card_total(self):
        self.assertEqual("You have a total of 11", self.cardgame.cards_total(self.cards))

