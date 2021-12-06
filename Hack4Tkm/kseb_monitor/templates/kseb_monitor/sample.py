# importing the required module
import matplotlib.pyplot as plt

# x axis values
x = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24]
# corresponding y axis values
y = [750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,750,]

# plotting the points
plt.plot(x, y)

# naming the x axis
plt.xlabel('Time')
# naming the y axis
plt.ylabel('Load in Kw')

# giving a title to my graph
plt.title("Hospital")

# function to show the plot
plt.show()
