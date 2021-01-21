from random import choice

class RandomWalk:
	"""Generates random walks."""

	def __init__(self, num_points=5000):
		"""Initializes walk attributes."""
		self.num_points = num_points

		# Walks start at (0, 0).
		self.x_values = [0]
		self.y_values = [0]

	def fill_walk(self):
		"""Calculate all the points in a walk."""

		# Keep calculating random steps until number of steps is reached.
		while len(self.x_values) < self.num_points:

			# Call get_step function for x and y.
			x_step = self.get_step()
			y_step = self.get_step()

			# Reject non-steps.
			if x_step == 0 and y_step == 0:
				continue

			# Calculate the new position.
			x = self.x_values[-1] + x_step
			y = self.y_values[-1] + y_step

			self.x_values.append(x)
			self.y_values.append(y)

	def get_step(self):
		"""Randomly determines the step direction and length."""
		self.direction = choice([1, -1])
		self.distance = choice([0, 1, 2, 3, 4, 5])
		self.step = self.direction * self.distance
		return self.step