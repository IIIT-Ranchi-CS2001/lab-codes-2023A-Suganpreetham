import matplotlib.pyplot as plt
import numpy as np
# Data for the two states
parties = ["BJP", "INC", "BSP", "Others"]
MadhyaPradesh = [163, 66, 0, 1]  
Rajasthan = [69, 115, 2, 13]  
# Define the x-axis positions for the bars
x = np.arange(len(parties))  # Positions for party names
bar_width = 0.35  # Width of each bar
# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(x - bar_width / 2, MadhyaPradesh, width=bar_width, label="Madhya Pradesh", color='blue')
plt.bar(x + bar_width / 2, Rajasthan, width=bar_width, label="Rajasthan", color='orange')
# Add labels, title, and legend
plt.xlabel("Parties", fontsize=12)
plt.ylabel("Seats Won", fontsize=12)
plt.title("Election Results by Party", fontsize=14)
plt.xticks(x, parties)  # Set party names as x-axis labels
plt.legend(title="States")
plt.grid(axis="y", linestyle="--", alpha=0.7)
# Show the plot
plt.tight_layout()
plt.show()