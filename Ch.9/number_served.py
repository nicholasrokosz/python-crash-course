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


restaurant = Restaurant("lou malnati's", 'deep dish pizza')

print(restaurant.number_served)
restaurant.set_number_served(100)
print(restaurant.number_served)
restaurant.increment_number_served(50)
print(restaurant.number_served)