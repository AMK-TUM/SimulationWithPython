import numpy as np
import random
import matplotlib.pyplot as plt

# Number of darts thrown
N = 100000

# Create an empty list to store x and y values which lies with in the circle
circlex = []
circley = []

# Create an empty list to store x and y values which lies with in the square
squarex = []
squarey = []

# Initialize i
i = 1

while i <= N:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x ** 2 + y ** 2 <= 1:
        circlex.append(x)
        circley.append(y)
    else:
        squarex.append(x)
        squarey.append(y)
    i += 1

pi = 4 * len(circlex) / float(N)


print(pi)


plt.plot(circlex, circley, "b.")
plt.plot(squarex, squarey, "g.")
plt.grid()
