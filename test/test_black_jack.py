import sys
sys.path.append("..")
from black_jack import BlackJack
import unittest


class TestBlackJack(unittest.TestCase):
	def setUp(self):
		self.black_jk = BlackJack(5, 100)
		for player in self.black_jk.players:
			player.bet(10)

	def test_deal_hands(self):
		self.black_jk.deal_hands()
		for player in self.black_jk.players:
			self.assertEqual(len(player.hands[0].cards), 2)
		self.assertEqual(len(self.black_jk.house.hand.cards), 2)



