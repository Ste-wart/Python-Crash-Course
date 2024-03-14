import matplotlib.pyplot as plt

values = range(1, 5001)
cubes = [x ** 2 for x in values]

fig, ax = plt.subplots()

ax.scatter(values, cubes)
plt.show()
