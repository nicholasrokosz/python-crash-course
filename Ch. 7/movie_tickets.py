prompt = "Enter your age: "

age = input(prompt)
age = int(age)

if age < 3:
	cost = 0
elif age < 12:
	cost = 10
else:
	cost = 15

print(f"The cost of your ticket is ${cost}.")