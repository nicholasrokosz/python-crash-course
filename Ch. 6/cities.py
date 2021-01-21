cities = {
	'tucson': {
		'country': 'america',
		'pop': 550_000,
		'founded': 1775,
		},
	'oslo': {
		'country': 'norway',
		'pop': 680_000,
		'founded': 1049,
		},
	'dublin': {
		'country': 'ireland',
		'pop': 1_400_000,
		'founded': 841,
		}
	}

for city, info in cities.items():
	print(f"{city.title()}")
	print(f"\tCountry: {info['country'].title()}")
	print(f"\tPopulation: ~{info['pop'] // 1000} thousand")
	if info['founded'] > 0:
		print(f"\tFounded: {info['founded']} CE\n")
	else:
		print(f"\tFounded: {-info['founded']} BCE\n")