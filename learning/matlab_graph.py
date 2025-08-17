import matplotlib.pyplot as plt

# Example: Line graph
x = [1, 2, 3, 4, 5]
y = [10, 14, 20, 25, 30]

plt.plot(x, y, marker='o')
plt.title("Line Graph Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()