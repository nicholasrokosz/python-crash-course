current_users = ['Nick', 'Nicole', 'Al', 'Pete', 'Michaela', 'Erin', 'Lauren']

new_users = ['Erin', 'Jake', 'Lauren', 'Tim']

current_users_lowercase = [user.lower() for user in current_users]

for user in new_users:
	if user.lower() in current_users_lowercase:
		print(f"{user.title()} is taken. Please select a new name.")
	else:
		print(f"{user.title()} is available.")