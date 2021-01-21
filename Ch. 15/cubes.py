import matplotlib.pyplot as plt

def plot_cubes(number_of_points):
	"""Produces a plot of cubic numbers."""

	x_values = range(1, number_of_points + 1)
	y_values = [x ** 3 for x in x_values]

	plt.style.use('grayscale')
	fig, ax = plt.subplots()
	ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.cool, s=5)

	ax.set_title("Square Numbers", fontsize=24)
	ax.set_xlabel("Value", fontsize=14)
	ax.set_ylabel("Square of Value", fontsize=14)
	ax.tick_params(axis='both', labelsize=14)

	plt.show()


plot_cubes(500)