import json

def get_fav_num():
	"""Asks a user for their favorite number and stores the value in a .json file."""

	fav_num = input("What is your favorite number? ")
	filename = 'fav_num.json'
	with open(filename, 'w') as f:
		json.dump(fav_num, f)


def print_fav_num():
	"""Retrieves user's favoite number and prints it."""

	filename = 'fav_num.json'
	
	with open(filename) as f:
		fav_num = json.load(f)
		
	print(f"I know your favorite number! It's {fav_num}.")