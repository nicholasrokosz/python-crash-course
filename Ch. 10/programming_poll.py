prompt = "Why do you like programming? (enter 'q' to exit)\n\t"

keep_going = True

while keep_going:
	reason = input(prompt)
	if reason != 'q':
		with open('programming_poll.txt', 'a') as file_object:
			file_object.write(f"{reason}\n")
	else:
		keep_going = False