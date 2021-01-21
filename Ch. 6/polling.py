favorite_languages = {
	'jen': 'python',
	'sarah': 'c',
	'edward': 'ruby',
	'phil': 'python',
	}

# for name, language in favorite_languages.items():
# 	print(f"{name.title()}'s favorite language is {language.title()}.")

perspective_pollers = ['phil', 'nick', 'al', 'nicole']

for person in perspective_pollers:
	if person in favorite_languages.keys():
		print("Thanks for responding to our poll!\n")
	else:
		print(f"Hi {person.title()}, please consider taking our poll!\n")