def add():
	"""Prompts the user for two numbers and then adds them."""

	print("Press 'q' to exit.")

	while True:
		x = input("First Number: ")
		if x == 'q':
			break
		y = input("Second Number: ")
		if y == 'q':
			break
		try:
			print(f"Sum: {int(x) + int(y)}\n")
		except ValueError:
			print("Oops, this program can only add numbers.\n")


add()