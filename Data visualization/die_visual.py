from collections import Counter

import plotly.express as px

from die import Die

die = Die()
results = [die.roll() for _ in range(100)]  # simulate n trials

freq = Counter(results)

# Visualize the results.
title = "Results of Rolling One D6 1,000 Times"
labels = {'x': 'Result', 'y': 'Frequency of Result'}

fig = px.bar(x=freq.keys(), y=freq.values(), title=title, labels=labels)
fig.show()
