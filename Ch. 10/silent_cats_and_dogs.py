def read_file(filename):
	try:
		with open(filename) as f:
			content = f.read()
		print(content.strip())

	except FileNotFoundError:
		pass

read_file('cats.txt')
read_file('dogs.txt')