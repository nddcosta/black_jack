from player import Player
from house import House
from deck import Deck



class InvalidInputError(Exception):
	pass


class BlackJack:
	def __init__(self, num_players, starting_money, num_decks=1):
		self.deck = Deck(num_decks)
		self.players = [Player(i, starting_money) for i in range(num_players)]
		self.house = House()


	def deal_hands(self):
		print("Dealing hands...")
		for player in self.players:
			player.deal_card(self.deck.deal1_card())
		self.house.deal_card(self.deck.deal1_card())
		for player in self.players:
			player.deal_card(self.deck.deal1_card())
		self.house.deal_card(self.deck.deal1_card())


	def print_player_information(self, player):
		print("Current money: ${}".format(player.current_money))
		for i, hand in enumerate(player.hands):
			print("Hand #{}".format(i+1))
			print("Bet on hand ${}".format(hand.bet))
			print(str(hand) + "\n")


	def valid_input(self, user_inputs, player, hand_num):
		if len(user_inputs) > 2:
			print("There needs to be one or two inputs")
			return False
		elif len(player.hands) < hand_num + 1:
			print("Hand num exceed number of hands")
			return False
		elif hand_num < 0:
			print("Hand num needs to be greater than or equal to 1")
			return False
		elif player.hands[hand_num].busted:
			print("Hand already busted")
			return False
		return True


	def print_help_info(self):
		print("[Type hit <hand num> to hit hand]")
		print("[Type double <hand num> to double down and hit hand]")
		print("[Type split <hand num> to split hand]")
		print("[Type stand <hand num> to stand on hand]")
		print("[Type info to see current player's info]")
		print("[Type show to see current card that house is showing]")
		print("<hand num> will default to Hand #1 if nothing is provided")


	def process_command(self, player, command, hand_num):
		if command == "show":
			print(self.house.showing_card())
		elif command == "info":
			self.print_player_information(player)
		elif command == "stand":
			player.stand_hand(hand_num)
		elif command == "split":
			player.split_hand(hand_num)
		elif command == "double":
			player.double_down_hand(hand_num, self.deck.deal1_card())
		elif command == "hit":
			player.hit_hand(hand_num, self.deck.deal1_card())
		else:
			print("Command not recognized")


	def process_input(self, player):
		hand_num = 0
		user_inputs = input().split()
		command = user_inputs[0]
		if len(user_inputs) == 2:
			try:
				hand_num = int(user_inputs[1]) - 1
			except ValueError:
				print("Hand num needs to be a number")
				raise ValueError
		if not self.valid_input(user_inputs, player, hand_num):
			raise InvalidInputError
		else:
			return command, hand_num			


	def play_player_hand(self, player):
		print("----Player {}'s turn----".format(player.player_num+1))
		self.print_help_info()
		while player.has_moves():
			self.print_player_information(player)
			try:
				command, hand_num = self.process_input(player)
			except (ValueError, InvalidInputError):
				continue
			self.process_command(player, command, hand_num)
	

	def collect_and_distribute_bets(self):
		print("----Wins and losses----")
		print("Final house hand: " + str(self.house.hand) + "\n")
		for player in self.players:
			for hand in player.hands:
				if hand.pushes(self.house.hand):
					player.push_bet(hand)
				else:
					if hand.beats(self.house.hand):
						player.take_bet(hand)
					else:
						player.lose_bet(hand)

	def clear_player_hands(self):
		for player in self.players:
			player.clear_hands()

	def play_house_hand(self):
		print("----House's turn----")
		while not self.house.hand.busted:
			if self.house.stay():
				break
			else:
				self.house.hit_hand(self.deck.deal1_card())

	def take_player_bets(self):
		for i, player in enumerate(self.players):
			print("Make bet Player {}".format(i+1))
			player.bet(int(input()))


	def play_round(self):
		self.clear_player_hands()
		self.take_player_bets()
		self.deal_hands()
		for player in self.players:
			self.play_player_hand(player)
		self.play_house_hand()
		self.collect_and_distribute_bets()

