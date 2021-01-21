favorite_places = {
	'nick': ['tucson', 'milwaukee'],
	'nicole': ['bend', 'sedona'],
	'al': ['madrid', 'barcelona', 'rome'],
	}

for person, places in favorite_places.items():
	print(f"{person.title()}'s favorite places are:")
	for place in places:
		print(place.title())
	print("\n")