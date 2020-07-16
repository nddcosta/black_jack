from hand import Hand

class House:
	def __init__(self):
		self.hand = Hand()

	def deal_card(self, card):
		self.hand.add_card(card)
	
	def showing_card(self):
		return self.hand.cards[0]

	def stay(self):
		if min(self.get_hand_values()) >= 17:
			return True
		return False

	def hit_hand(self, card):
		self.hand.hit(card)

	def get_hand_values(self):
		return self.hand.get_total_values()
