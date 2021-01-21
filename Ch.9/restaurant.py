"""A class that can be used to represent a restaurant."""

class Restaurant:
	"""Describes a restaurant simply."""
	def __init__(self, restaurant_name, cuisine_type):
		"""initialize restaurant name and cuisine type attributes"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type

	def describe_restaurant(self):
		"""describes a restaurant by its name and cuisine type"""
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

	def open_restaurant(self):
		"""Prints a message that the restaurant is open."""
		print(f"The restaurant is open.")