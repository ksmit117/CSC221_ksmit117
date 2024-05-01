import plotly.express as px
from die import Die

# Creates three D6 die
die_1 = Die()
die_2 = Die()
die_3 = Die()

#adds up the rolls of 3 d6 die
results = []
for roll_num in range(1000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)
    
#analyze the results
frequencies = []
max_result = die_1.num_sides + die_2.num_sides + die_3.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
#visualize the results
title = "Results of Rolling Three D6 dice 1000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}
fig = px.bar(x=poss_results, y=frequencies, title=title, labels=labels)
fig.update_layout(xaxis_dtick=1)
fig.write_html('dice_visual_d6d10.html')
fig.show()