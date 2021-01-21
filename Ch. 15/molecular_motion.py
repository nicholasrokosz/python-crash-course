import matplotlib.pyplot as plt

from modified_random_walks import RandomWalk

# Keep running until user quits.
while True:
	# Make a random walk instance.
	rw = RandomWalk(250)
	rw.fill_walk()

	# Plot the walk points.
	plt.style.use('classic')
	fig, ax = plt.subplots(figsize=(5, 3), dpi=227)
	point_numbers = range(rw.num_points)
	ax.plot(rw.x_values, rw.y_values, linewidth=1)

	# Emphasize the first and last points.
	ax.scatter(0, 0, c='green', edgecolors='none', s=50)
	ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red',
		edgecolors='none', s=50)

	# Remove the axes.
	ax.get_xaxis().set_visible(False)
	ax.get_yaxis().set_visible(False)

	plt.show()

	another = input("Make another random walk? (y/n): ")
	if another == 'n':
		break