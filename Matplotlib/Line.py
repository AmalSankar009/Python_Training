import matplotlib.pyplot as plt
import numpy as np

y1 = np.array([-3, 8, 1, 10])
y2 = np.array([6, 2, 7, 11])
y3 = np.array([5,5,5,5,5])

plt.plot(y1, ls=':')
plt.plot(y2, ls="-")
plt.plot(y3)

plt.title("PLOT")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")

plt.show()