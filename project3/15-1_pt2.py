import matplotlib.pyplot as plt
plt.style.available

x_values = range(1, 5000)
y_values = [x**3 for x in x_values]

plt.style.use('Solarize_Light2')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.rainbow, s=1)

#set chart title and label axis
ax.set_title("Cubic Numbers", fontsize=24)
ax.set_xlabel("Value", fontsize=14)
ax.set_ylabel("cubic of Value", fontsize=14)

#set size of tick labels
ax.tick_params(labelsize=14)

#set the range of each axis
ax.ticklabel_format(style='plain')



plt.savefig('squares_plot.png', bbox_inches='tight')
plt.show()
