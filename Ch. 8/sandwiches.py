def sandwich(*toppings):
	print("Your sandwich will be made with these ingredients:")
	for topping in toppings:
		print(f"- {topping}")

sandwich('provolone', 'ham', 'turkey', 'lettuce', 'tomato')

sandwich('ham', 'swiss')