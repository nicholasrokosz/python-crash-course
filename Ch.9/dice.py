from random import randint

class Die:
	"""Represents a die."""

	def __init__(self, sides=6):
		self.sides = sides

	def roll_die(self):
		print(f"The {self.sides}-sided die rolled a {randint(1, self.sides)}")


six_sided_die = Die()
six_sided_die.roll_die()