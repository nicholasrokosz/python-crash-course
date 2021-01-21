prompt = "Enter a topping you'd like. "
prompt += "Enter quit when you're finished.\nTopping: "

while True:
	topping = input(prompt)
	
	if topping == 'quit':
		break
	else:
		print(f"Adding {topping} to your pizza.\n")
