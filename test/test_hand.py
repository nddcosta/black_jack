import sys
sys.path.append("..")
import unittest
from hand import Hand
from card import Card, Rank, Suite

class TestHand(unittest.TestCase):
	def setUp(self):
		self.hand = Hand()
		self.house_hand = Hand()
		self.card1 = Card(Suite.DIAMONDS, Rank.TWO)
		self.card2 = Card(Suite.DIAMONDS, Rank.JACK)
		self.card3 = Card(Suite.CLOVERS, Rank.TEN)
		self.card4 = Card(Suite.DIAMONDS, Rank.ACE)

	def test_pushes(self):
		self.hand.add_card(self.card2)
		self.hand.add_card(self.card4)
		self.house_hand.add_card(self.card3)
		self.house_hand.add_card(self.card4)
		self.assertTrue(self.hand.pushes(self.house_hand))

	def test_beats_lose(self):
		self.hand.add_card(self.card1)
		self.hand.add_card(self.card3)
		self.house_hand.add_card(self.card1)
		self.house_hand.add_card(self.card4)
		self.assertFalse(self.hand.beats(self.house_hand))

	def test_beats_win(self):
		self.hand.add_card(self.card3)
		self.hand.add_card(self.card4)
		self.house_hand.add_card(self.card1)
		self.house_hand.add_card(self.card4)
		self.assertTrue(self.hand.beats(self.house_hand))

	def test_add_card(self):
		size_before = len(self.hand.cards)
		self.hand.add_card(self.card1)
		size_after = len(self.hand.cards)
		self.assertGreater(size_after, size_before)

	def test_hit_bust(self):
		self.hand.hit(self.card1)
		self.hand.hit(self.card2)
		self.hand.hit(self.card3)
		self.assertTrue(self.hand.busted)

	def test_hit_no_bust(self):
		self.hand.hit(self.card2)
		self.hand.hit(self.card4)
		self.assertFalse(self.hand.busted)

	def test_split(self):
		self.hand.add_card(self.card1)
		self.hand.add_card(self.card2)
		size_before = len(self.hand.cards)
		self.hand.split()
		size_after = len(self.hand.cards)
		self.assertLess(size_after, size_before)

	def test_get_total_values_no_ace(self):
		self.hand.add_card(self.card2)
		self.hand.add_card(self.card3)
		values = self.hand.get_total_values()
		self.assertEqual(len(values), 2)
		self.assertEqual(values[0], 20)
		self.assertEqual(values[1], 20)

	def test_get_total_values_with_ace(self):
		self.hand.add_card(self.card3)
		self.hand.add_card(self.card4)
		values = self.hand.get_total_values()
		self.assertEqual(len(values), 2)
		self.assertTrue(11 in values)
		self.assertTrue(21 in values)
