fav_nums = {
	'nick': [555, 21, 3],
	'al': [1, 7, 100],
	"nicole": [2, 4, 10],
	}

#print(f"Nick's favorite number is {fav_nums['nick']}")

for name, nums in fav_nums.items():
	print(f"{name.title()}'s favorite numbers are:")
	for num in nums:
		print(num)