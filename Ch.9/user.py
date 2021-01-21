class User:
	""""""
	def __init__(self, first_name, last_name, location, age):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.age = age
		self.login_attempts = 0

	def describe_user(self):
		"""Prints a message describing the user."""
		print(f"\n{self.first_name.title()} {self.last_name.title()} is "
			f"{self.age} years old and lives in {self.location.title()}.")

	def greet_user(self):
		print(f"Hello, {self.first_name.title()}!")

	def increment_login_attempts(self):
		self.login_attempts += 1

	def reset_login_attempts(self):
		self.login_attempts = 0