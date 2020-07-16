from random import shuffle
from card import Card, Rank, Suite

class Deck:
	def __init__(self, num_decks):
		self.num_decks = num_decks
		self.deck = list()
		self.__load_deck()

	def __load_deck(self):
		for i in range(self.num_decks):
			for rank in Rank:
				for suite in Suite:
					self.deck.append(Card(suite, rank))
		self.shuffle_deck()

	def shuffle_deck(self):
		shuffle(self.deck)

	def deal1_card(self):
		if not self.deck:
			self.__loadDeck()
		return self.deck.pop()
		