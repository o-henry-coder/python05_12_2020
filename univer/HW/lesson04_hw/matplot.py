import matplotlib.pyplot as plt

left_edges = [0, 1, 2, 3, 4]
heights = [0, 3, 1, 5, 2]

plt.bar(left_edges, heights)
plt.title('this is table')

plt.xlabel('this is x')
plt.ylabel('this is y')

plt.grid(True)

plt.show()