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


restaurant_0 = Restaurant("lou malnati's", 'deep dish pizza')
restaurant_1 = Restaurant('in n out', 'burgers')
restaurant_2 = Restaurant('time market', 'neopolitan pizza')

restaurant_0.describe_restaurant()
restaurant_1.describe_restaurant()
restaurant_2.describe_restaurant()