class Restaurant:
	"""Describes a restaurant simply."""
	def __init__(self, restaurant_name, cuisine_type):
		"""initialize restaurant name and cuisine type attributes and sets
		number served attribute to a default value 0"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0

	def describe_restaurant(self):
		"""describes a restaurant by its name and cuisine type"""
		print(f"{self.restaurant_name.title()} serves {self.cuisine_type}.")

	def open_restaurant(self):
		"""Prints a message that the restaurant is open."""
		print(f"The restaurant is open.")

	def set_number_served(self, customers_served):
		self.number_served = customers_served

	def increment_number_served(self, increment):
		self.number_served += increment

class IceCreamStand(Restaurant):
	"""Models an ice cream stand."""

	def __init__(self, restaurant_name, cuisine_type):
		"""Initialize attributes of the parent class, Restaurant."""
		super().__init__(restaurant_name, cuisine_type)

	def flavors(self, *flavors):
		self.flavors = flavors

	def display_flavors(self):
		print("Available flavors:")
		for flavor in self.flavors:
			print(f"\t-{flavor}")


sweet_republic = IceCreamStand('sweet republic', 'ice creamery')

sweet_republic.flavors('vanilla', 'chocolate', 'butter pecan')
sweet_republic.display_flavors()