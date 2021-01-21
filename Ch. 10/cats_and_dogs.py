def read_file(filename):
	try:
		with open(filename) as f:
			content = f.read()
		print(content.strip())

	except FileNotFoundError:
		print(f"We couldn't find {filename}")

read_file('cats.txt')
read_file('dogs.txt')