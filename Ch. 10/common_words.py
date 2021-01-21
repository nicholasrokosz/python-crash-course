filename = 'moby_dick.txt'

with open(filename) as f:
	content = f.read()

print(content.lower().count('whale'))