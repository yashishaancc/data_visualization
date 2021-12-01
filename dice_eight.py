import pygal
from die import Die
# Create a D6.
die1 = Die(8)
die2 = Die(8)
# Make some rolls, and store results in a list.
results = []
for roll_num in range(1000):
	result = die1.roll()+die2.roll()
	results.append(result)
# Analyze the results.
frequencies = []
max_result = die1.num_sides+die2.num_sides
for value in range(2, max_result+1):
	frequency = results.count(value)
	frequencies.append(frequency)
# print(frequencies)
# print(results)
# Visualize the results.
hist = pygal.Bar()
hist.title = "Results of rolling two D8 dice 1000 times."
hist.x_labels = [str(i) for i in range(2, 17)]
hist.x_title = "Result"
hist.y_title = "Frequency of Result"
hist.add('D8+D8', frequencies)
hist.render_to_file('dice_eight_visual.svg')