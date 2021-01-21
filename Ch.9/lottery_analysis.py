from random import choice

def run_lottery():
	""""""
	lottery_chars = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'a', 'b,' 'c', 'd', 'e']

	winner = []

	#print("The winning combination is:")
	while len(winner) < 4:
		pulled_char = choice(lottery_chars)
		if pulled_char not in winner:
			winner.append(pulled_char)
	return(winner)

my_ticket = ['e', 0, 'a', 5]
number_of_picks = 0

while my_ticket != run_lottery():
	run_lottery()
	number_of_picks += 1

print(f"My ticket: {my_ticket}")
print(f"Number of picks to get my ticket: {number_of_picks}")