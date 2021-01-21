from math import sqrt

def find_mean(dataset):
	'''Finds the mean of a list of lists.'''
	total_height = 0
	num = 0

	for row in dataset:
		height = row[1]
		total_height += height
		num += 1

	return total_height / num


def find_variance(dataset):
	'''Finds the variance of a list of lists.'''
	total = 0
	counter = 0
	mean = find_mean(dataset)

	for row in dataset:
		height = row[1]
		distance_squared = (abs(height - mean)) ** 2
		total += distance_squared
		counter += 1

	variance = total / counter
	return variance

def find_standard_deviation(dataset):
	v = find_variance(dataset)
	standard_deviation = sqrt(v)
	return standard_deviation

my_dataset = [
		['Nick', 74],
		['Elana', 66],
		['Dinah', 68],
		['Rebecca', 69],
		['Ben', 73],
		['Charu', 70]
]


print(find_mean(my_dataset))
print(find_variance(my_dataset))
print(find_standard_deviation(my_dataset))