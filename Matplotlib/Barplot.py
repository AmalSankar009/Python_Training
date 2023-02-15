import matplotlib.pyplot as plt
import numpy as np

x = np.array(["A", "B", "C", "D","E","F"])
y = np.array([3, 8, 1,-5,10,.5])
l = np.array([0,0,0,0,0,0])
plt.plot(l, color='black')
plt.bar(x,y)
plt.show()