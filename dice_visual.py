import pygal
from die import Die
# Create a D6.
die1 = Die()
die2 = Die()
die3 = Die()
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die1.roll()+die2.roll()+die3.roll()
	results.append(result)
# Analyze the results.
frequencies = []
max_result = die1.num_sides+die2.num_sides+die3.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
# print(frequencies)
# print(results)
# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling three D6 dice 1000 times."
hist.x_labels = [str(i) for i in range(3, 19)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D6+D6', frequencies)
hist.render_to_file('dice_visual.svg')