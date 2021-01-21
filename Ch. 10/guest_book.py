prompt = "Please enter your name (enter 'q' when finished): "

keep_going = True

with open('guest_book.txt', 'a') as file_object:
	while keep_going:
		name = input(prompt)
		if name != 'q':
			print(f"Welcome, {name.title()}")
			file_object.write(f"{name.title()}\n")
		else:
			keep_going = False

