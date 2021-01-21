class User:
	""""""
	def __init__(self, first_name, last_name, location, age):
		self.first_name = first_name
		self.last_name = last_name
		self.location = location
		self.age = age

	def describe_user(self):
		"""Prints a message describing the user."""
		print(f"\n{self.first_name.title()} {self.last_name.title()} is "
			f"{self.age} years old and lives in {self.location.title()}.")

	def greet_user(self):
		print(f"Hello, {self.first_name.title()}!")


user_0 = User('nick', 'rokosz', 'scottsdale', 23)
user_1 = User('alex', 'rokosz', 'tucson', 23)
user_2 = User('peter', 'rokosz', 'minneapolis', 29)

user_0.describe_user()
user_0.greet_user()

user_1.describe_user()
user_1.greet_user()

user_2.describe_user()
user_2.greet_user()