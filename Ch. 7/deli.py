sandwich_orders = ['blt', 'pb & j', 'ham & swiss', 'grilled cheese']

finished_sandwiches = []

while sandwich_orders:
	current_sandwich = sandwich_orders.pop()
	print(f"I made your {current_sandwich}.")
	finished_sandwiches.append(current_sandwich)

print("\nReady sandwiches:")

for sandwich in finished_sandwiches:
	print(sandwich)