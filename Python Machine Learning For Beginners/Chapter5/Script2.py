import matplotlib.pyplot as plt
import numpy as np
import math

x_vals = np.linspace(0, 20, 20)
y_vals = [math.sqrt(i) for i in x_vals]

fig = plt.figure()
ax = plt.axes()
ax.plot(x_vals, y_vals)

plt.show()
