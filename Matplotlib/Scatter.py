import matplotlib.pyplot as plt
import numpy as np

x=np.array([1,2,3,4,5,6,7,8])
y=np.array([10,11,12,13,14,15,16,17])
s1=([1,1,1,1,1,1,1,1])
x1=np.array([11,22,33,44,55,66,77,88])
y1=np.array([34,56,78,13,89,44,27,99])

plt.scatter(x,y,s=s1)
plt.scatter(x1,y1, color='yellow')

plt.show()