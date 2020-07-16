from black_jack import BlackJack

if __name__ == '__main__':
	print("------Black Jack------")
	num_players = input("How many players are playing? [int]")
	intial_money = input("How much money is each player starting with? [int]")
	black_j = BlackJack(int(num_players), int(intial_money))
	while True:
		black_j.play_round()
		user_input = input("Keep playing? [y/n]")
		if user_input == 'n':
			break
