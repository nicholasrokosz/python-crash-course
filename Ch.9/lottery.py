from random import choice

def lottery():
	""""""
	lottery_chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b,' 'c', 'd', 'e']

	winner = []

	print("The winning combination is:")
	while len(winner) < 4:
		pulled_char = choice(lottery_chars)
		if pulled_char not in winner:
			winner.append(pulled_char)
	print(winner)


lottery()