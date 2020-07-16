from hand import Hand

class Player:
	def __init__(self, player_num, starting_money):
		self.player_num = player_num
		self.current_money = starting_money
		self.hands = list()

	def has_moves(self):
		for hand in self.hands:
			if not hand.busted and not hand.stand:
				return True
		return False

	def clear_hands(self):
		self.hands.clear()

	def take_bet(self, hand):
		print("Player {} won ${}".format(self.player_num, hand.bet))
		print("Winning hand: " + str(hand) + "\n")
		self.current_money += hand.bet

	def push_bet(self, hand):
		print("Player {} pushed".format(self.player_num))
		print("Pushed hand: " + str(hand) + "\n")


	def lose_bet(self, hand):
		print("Player {} lost ${}".format(self.player_num, hand.bet))
		print("Losing hand: " + str(hand) + "\n")
		self.current_money -= hand.bet

	def deal_card(self, card):
		self.hands[0].add_card(card)

	def hit_hand(self, hand_num, card):
		self.hands[hand_num].hit(card)

	def stand_hand(self, hand_num):
		self.hands[hand_num].stand = True

	def double_down_hand(self, hand_num, card):
		self.hands[hand_num].double_bet()
		self.hit_hand(hand_num, card)
		self.hands[hand_num].stand
	
	def split_hand(self, hand_num):
		self.hands.append(Hand(self.hands[hand_num].bet))
		self.hands[-1].add_card(self.hands[hand_num].split())
	
	def get_hand_values(self, hand_num):
		return self.hands[hand_num].get_total_values()

	def bet(self, bet):
		self.hands.append(Hand(bet))
		
	
	