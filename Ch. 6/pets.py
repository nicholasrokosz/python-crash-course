randy = {'animal': 'dog', 'owner': 'pete'}
jane = {'animal': 'dog', 'owner': 'nicole'}
luke = {'animal': 'cat', "owner": 'schwarz'}
louie = {'animal': 'cat', 'owner': 'lauren'}

pets = [randy, jane, luke, louie]

for pet in pets:
	print(f"{pet['owner'].title()} has a pet {pet['animal']}.\n")