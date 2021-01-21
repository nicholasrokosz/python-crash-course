users = ['admin', 'Nick', 'Nicole', 'Al', 'Pete', 'Michaela']

for user in users:
	if user == 'admin':
		print("Hello admin, would you like to see a status report?")
	else:
		print(f"Hello {user}, thanks for logging in.")