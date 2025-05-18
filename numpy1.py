#Import numpy as np
import numpy as np
import matplotlib.pyplot as plt

# # Create an array of 100 evenly spaced numbers 0 to 100 using Numpy and save it to variable x

x = np.linspace(0 , 10 , 100)

# # Create a plot using plt.subplots() and plot x versues x^2 (x squared)
# fig, ax = plt.subplots()
# ax.plot(x, x**2)
# plt.show()

# import numpy1 as np
# import matplotlib.pyplot as plt

# x = np.linspace(0, 10, 100)
# y = x**2 

# plt.plot(x, y)
# plt.xlabel('x')
# plt.ylabel('y')
# plt.title('Plot of y = x^2')
# plt.grid(True)
# plt.show()

# Create a scatter plot of x versus the exponential of x (np.exp(x))
fig, ax =plt.subplots()
ax.scatter(x, np.exp(x))
plt.show()