users = []

if users:
	for user in users:
		if user == 'admin':
			print("Hello admin, would you like to see a status report?")
		else:
			print(f"Hello {user}, thanks for logging in.")
else:
	print("We need to find some users!")