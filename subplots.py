import matplotlib.pyplot as plt
import numpy as np
# Data for the first pie chart
y = np.array([163, 66, 0, 1])
mylabels = ["BJP", "INC", "BSP", "Others"]
myexplode = [0.1, 0, 0, 0]
# Data for the second pie chart
z = np.array([69, 115, 2, 13])
mylabels2 = ["INC", "BJP", "BSP", "Others"]
myexplode2 = [0, 0.1, 0, 0]
# Create a figure with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))
# First pie chart
ax1.pie(y, labels=mylabels, explode=myexplode, autopct='%1.1f%%', startangle=90)
ax1.set_title('Chart 1: Party Distribution 1')
# Second pie chart
ax2.pie(z, labels=mylabels2, explode=myexplode2, autopct='%1.1f%%', startangle=15)
ax2.set_title('Chart 2: Party Distribution 2')
# Adjust layout and display the figure
plt.tight_layout()
plt.show() 