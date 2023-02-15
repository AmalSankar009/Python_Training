import matplotlib.pyplot as plt
import numpy as np

y = np.array([40, 20, 15, 15])
l=(["A","B","C","D"])

plt.pie(y,labels=l,startangle=90,shadow=True)
plt.legend()
plt.show() 