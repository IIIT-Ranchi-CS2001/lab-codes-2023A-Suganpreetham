import matplotlib.pyplot as plt
import numpy as np
y = np.array([163,66,0,1])
mylabels = ["BJP", "INC", "", "Others(1) BSP(0)"]
myexplode = [0.1, 0, 0, 0]

plt.pie(y, labels = mylabels, explode = myexplode)
plt.show() 

z = np.array([69,115,2,13])
mylabels2 = ["INC", "BJP", "BSP", "Others"]
myexplode2 = [0, 0.1, 0, 0]

plt.pie(z, labels = mylabels2, explode = myexplode2)
plt.show() 
