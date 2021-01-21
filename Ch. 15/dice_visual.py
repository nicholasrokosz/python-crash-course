from plotly.graph_objs import Bar, Layout

from plotly import offline

from die import Die

# Create two instances of D6.
die_1 = Die()
die_2 = Die()

# Rolls the die a number of times and records results in a list.
# results = []
# for roll_num in range(1_000_000):
# 	result = die_1.roll() + die_2.roll()
# 	results.append(result)
results = [die_1.roll() + die_2.roll() for roll_num in range(1_000_000)]

# Analyze the results.
# frequencies = []
max_result = die_1.num_sides + die_2.num_sides
# for value in range(2, max_result+1):
# 	frequency = results.count(value)
# 	frequencies.append(frequency)
frequencies = [results.count(value) for value in range(2, max_result+1)]

# Visualize the results.
x_values = list(range(2, max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}
my_layout = Layout(title='Results of rolling two D6 dice 1,000,000 times',
	xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d6.html')