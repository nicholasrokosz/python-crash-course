def build_deck():
	"""Builds a deck of cards (ace high) into a dictionary."""
	suits = {
		'hearts': [],
		'diamonds': [],
		'clubs': [],
		'spades': []
		}

	face_cards = ['jack','queen', 'king', 'ace']

	for suit in suits.keys():
		for number in range(1,11):
			suits[suit].append(f'{number} of {suit.title()}')
		for face_card in face_cards:
			suits[suit].append(f'{face_card.title()} of {suit.title()}')


	return suits


deck = build_deck()
print(deck['hearts'])