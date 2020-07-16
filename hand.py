from card import Card

class Hand:
	def __init__(self, bet=0):
		self.cards = list()
		self.bet = bet
		self.busted = False
		self.stand = False


	def pushes(self, house_hand):
		if not self.busted and not house_hand.busted:
			return max(self.get_total_values()) == max(house_hand.get_total_values())
		return False

	def beats(self, house_hand):
		if self.busted:
			return False
		elif house_hand.busted:
			return True
		else:
			if(max(self.get_total_values()) > max(house_hand.get_total_values())):
				return True
			else:
				return False

	def add_card(self, card):
		self.cards.append(card)
	
	def hit(self, card):
		self.add_card(card)
		if min(self.get_total_values()) > 21:
			self.busted = True

	def double_bet(self):
		self.bet += self.bet

	def stand(self):
		self.stand = True

	def split(self):
		if len(self.cards) > 1:
			return self.cards.pop()
	
	def __str__(self):
		hand_str = "".join([str(card) for card in self.cards])
		if self.busted:
			hand_str = "BUSTED" + hand_str
		return hand_str

	def get_total_values(self):
		totals = [0,0]
		for card in self.cards:
			card_values = card.get_value()
			totals[0] += card_values[0]
			totals[1] += card_values[1]
		return totals