dream_vacation = {}

name = input("What's your name? ")	
location = input("Where would you like to go on vacation? ")

dream_vacation[name] = location

print("\nThanks for taking our poll!\nResults of poll:")
print(f"{name.title()} wants to visit {location.title()}.")