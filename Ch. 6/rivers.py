rivers = {
	'mississippi': 'america',
	'thames': 'england',
	'seine': 'france'
	}

for river, country in rivers.items():
	print(f"The {river.title()} runs through {country.title()}.")

print("\nThese rivers are mentioned:")
for river in rivers.keys():
	print(f"{river.title()}")

print("\nThese countries are mentioned:")
for country in rivers.values():
	print(f"{country.title()}")