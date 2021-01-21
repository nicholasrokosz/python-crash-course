twin = {
	'age': 23,
	'city': 'tucson',
	'first_name': 'alexander',
	'last_name': 'rokosz',
	}

# print(twin['age'])
# print(twin['city'])
# print(twin['first_name'])
# print(twin['last_name'])

older_brother = {
	'age': 29,
	'city': 'minneapolis',
	'first_name': 'peter',
	'last_name': 'rokosz',
	}

girlfriend = {
	'age': 23,
	'city': 'gilbert',
	'first_name': 'nicole',
	'last_name': 'callahan',
	}

people = [twin, older_brother, girlfriend]

for person in people:
	print(f"{person['first_name'].title()} {person['last_name'].title()}"
	f" is {person['age']} years old and lives in {person['city'].title()}.\n")




