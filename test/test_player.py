import sys
sys.path.append("..")
from player import Player
from card import Card, Rank, Suite
import unittest

class TestPlayer(unittest.TestCase):
	def setUp(self):
		self.player = Player(0, 100)
		self.card1 = Card(Suite.DIAMONDS, Rank.ACE)
		self.card2 = Card(Suite.HEARTS, Rank.ACE)
		self.card3 = Card(Suite.CLOVERS, Rank.THREE)

	def test_double_down_hand(self):
		self.assertEqual(self.player.current_money, 100)
		self.player.bet(50)
		self.player.deal_card(self.card1)
		self.player.deal_card(self.card2)
		self.player.double_down_hand(0, self.card3)
		self.assertEqual(self.player.hands[0].bet, 100)
	
	def test_bet(self):
		self.assertEqual(self.player.current_money, 100)
		self.player.bet(30)
		self.assertEqual(len(self.player.hands), 1)
		self.assertEqual(self.player.hands[0].bet, 30)

	def test_split_hand(self):
		self.player.bet(30)
		self.player.deal_card(self.card1)
		self.player.deal_card(self.card2)
		self.assertEqual(len(self.player.hands), 1)
		self.player.split_hand(0)
		self.assertEqual(len(self.player.hands), 2)
		self.assertEqual(len(self.player.hands[0].cards), 1)
		self.assertEqual(len(self.player.hands[1].cards), 1)
		self.assertEqual(self.player.hands[0].bet, 30)
		self.assertEqual(self.player.hands[1].bet, 30)
		self.assertIn(self.card1, self.player.hands[0].cards)
		self.assertIn(self.card2, self.player.hands[1].cards)

