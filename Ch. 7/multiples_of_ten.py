num = input("Enter a number: ")
num = int(num)

if num % 10 == 0 and num != 0:
	print(f"{num} is a multiple of 10.")
else:
	print(f"{num} is not a multiple of 10.")