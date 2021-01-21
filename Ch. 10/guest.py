prompt = "Please enter your name: "

name = input(prompt)

filename = 'guest.txt'

with open(filename, 'a') as file_object:
	file_object.write(name)