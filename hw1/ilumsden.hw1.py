"""
Homework 1
Name: Ian Lumsden
NetID: ilumsden

This script calculates a running average of the high temperatures
in Knoxville, TN, in August 2013. This data is printed to the console.
Then, this data and the original high temperature data is graphed using
MatPlotLib.
"""

import numpy as np
import matplotlib.pyplot as plt

xData = np.arange(1,32)    # Ranges for x and y axes must match
# The high temperature data
tData = [86,87,84,86,86,86,84,83,90,89,88,85,86,79,83,81, \
         75,80,81,85,81,88,89,87,84,85,86,88,88,90,90]
# The high temperature data is converted to a NumPy array for ease of use.
tData = np.array(tData)
# avg is a NumPy array that stores the cumulative sum of the tData array.
avg = np.cumsum(tData, dtype=float)
# The average temperatures are calculated by dividing each element by its index plus 1.
avg = avg / (1 + np.indices(avg.shape))
# The average temperature data is printed through stdout.
print("Average Temperatures:")
for a in np.nditer(avg):
    print("{:.2f}".format(a))
# The line for the high temperature data is created so that it is a blue solid line.
plt.plot(xData, tData, "b-")
# The points for the high temperature data are added to the plot as red dots.
plt.scatter(xData, tData, color="red")
# The average data is added as a green dashed line
plt.plot(xData, avg[0], "g--")
# The X and Y axes are resized, and their limits are set.
plt.xlim(xmin=0)
plt.ylim(ymin=(10*(tData.min() // 10)), ymax=95)
plt.yticks(np.arange(plt.ylim()[0], plt.ylim()[1], step=5))
# A label is added for the average line
plt.text(15, 86, "Monthly Avg", color="green")
# A grid is added to the graph
plt.grid()
# A title is added to the plot, along with labels for the axes.
plt.title("High Temperatures for Knoxville, TN - August 2013")
plt.xlabel("Day")
plt.ylabel("High Temp")
# The plot is generated.
plt.show()

