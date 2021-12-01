import matplotlib.pyplot as plt
x_values = list(range(1,5001))
y_values = [x**3 for x in x_values]
plt.scatter(x_values, y_values, c = y_values, cmap = plt.cm.Blues,
	edgecolor = 'none', s = 40)
# Set chart title and label axes.
plt.title("Cube Numbers", fontsize = 24)
plt.xlabel("Value", fontsize = 14)
plt.ylabel("Cube of Value", fontsize = 14)
# Set size of tick labels.
plt.tick_params(axis = 'both', which = 'major', labelsize = 14)
# Set the range for each axis.
plt.axis([0, 5100, 0, 135000000000])
plt.savefig('cubes_plot.png', bbox_inches = 'tight')
plt.show()