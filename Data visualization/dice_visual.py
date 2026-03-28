from collections import Counter

import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

from die import Die

die = Die()

sim1 = die.simulation(1000)
sim2 = die.simulation(1000)  # simulate n trials

results = Die.dice(sim1, sim2)

freq = Die.frequency(results)

# Visualize the results.
title = "Results of Rolling Two D6 Dice 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=freq.keys(), y=freq.values(), title=title, labels=labels)
#
# # Further customize chart.
# fig.update_layout(xaxis_dtick=1)
# # fig.write_html('dice_visual.xhtml')
# fig.show()

#
sns.barplot(x=freq.keys(), y=freq.values())
plt.show()
