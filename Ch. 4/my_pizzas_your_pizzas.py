pizzas = ['deep dish', 'margherita', 'classic cheese']
for pizza in pizzas:
	print(f"I like {pizza} pizza.")
print("\nI really love pizza!")

friend_pizzas = pizzas[:]
pizzas.append('hawaiian')
friend_pizzas.append('pepperoni')

print("\nMy favorite pizzas are:")
for pizza in pizzas:
	print(pizza)

print("\nMy friend's favorite pizzas are:")
for pizza in friend_pizzas:
	print(pizza)