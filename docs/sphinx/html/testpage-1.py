# This figure is a test
import numpy as np
import matplotlib.pyplot as plt

x = np.arange(11)
y = x**2

fig, ax = plt.subplots()
ax.plot(x, y)
#fig.show()