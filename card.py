from enum import Enum

class Suite(Enum):
	DIAMONDS = 1
	HEARTS = 2
	CLOVERS = 3
	SPADES = 4
	
class Rank(Enum):
	ACE = 1
	TWO = 2
	THREE = 3
	FOUR = 4
	FIVE = 5 
	SIX = 6 
	SEVEN = 7
	EIGHT = 8
	NINE = 9
	TEN = 10
	JACK = 11
	QUEEN = 12
	KING = 13

class Card:
	def __init__(self, suite, rank):
		self.suite = suite
		self.rank = rank
	
	def get_value(self):
		if self.rank == Rank.ACE:
			return (1,11)
		elif self.rank == Rank.JACK or self.rank == Rank.QUEEN or self.rank == Rank.KING:
			return (10, 10)
		else:
			return (self.rank.value, self.rank.value)
			
	def __str__(self):
		return "\n{} of {}".format(self.rank.name, self.suite.name)
