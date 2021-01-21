filename = 'learning_python.txt'

with open(filename) as file_object:
	lines = file_object.readlines()

for line in lines:
	print(line.strip())


with open(filename) as file_object:
	content = file_object.read()

print(content.strip())


with open(filename) as file_object:
	for line in file_object:
		print(line.strip())