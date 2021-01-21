from user import User


# class Privileges:
# 	"""Models user privileges."""
# 	def __init__(self):
# 		"""Initialize attributes."""
# 		self.privileges = ['can add post', 'can delete post', 'can ban users']

# 	def show_privileges(self):
# 		"""Displays admin privileges."""
# 		print("Admin privileges:")
# 		for privilege in self.privileges:
# 			print(f"\t-{privilege}")


class Admin(User):
	"""Models an administrative user."""
	def __init__(self, first_name, last_name, location, age):
		"""Initialize attributes of parent class, User."""
		super().__init__(first_name,last_name,location,age)
		self.privileges = Privileges()


class Privileges:
	"""Models user privileges."""
	def __init__(self):
		"""Initialize attributes."""
		self.privileges = ['can add post', 'can delete post', 'can ban users']

	def show_privileges(self):
		"""Displays admin privileges."""
		print("Admin privileges:")
		for privilege in self.privileges:
			print(f"\t-{privilege}")



