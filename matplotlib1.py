
import matplotlib.pyplot as plt

# print(plt.plot())

# plt.plot([2,4,6,8])

# print(plt.show())

# # Create two lists, one called X, one called Y, each with 5 numbers in them

# x = [22,88,103,45]
# y = [7,8,9,10]

# # Plot X & Y (the lists you've created)

# plt.plot(x,y)

# #Create a plot using plt.subplot()

# fig, ax = plt.subplos()
# ax.plot(X, y)

# Prepared data (create two lists of 5 numbers x & y)

x = [34, 77, 21, 54, 9]
y = [9, 45, 89, 66, 4]

# setup figure and axes using plt.subplots()
fig, ax = plt.subplots()

# Add daqta (x,y) to axes
ax.plot(x,y)

#Customize Plot by adding a title, xlabel and ylabel
ax.set(title = "SImple simple plot",
       xlabel ="x-axes",
       ylabel = "y-axes")

#save the plot to file using fig.savefig()

fig.savefig("./image.jpeg")