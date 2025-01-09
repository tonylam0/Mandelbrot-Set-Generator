import numpy
import matplotlib

# Iterative formula
# c represents a complex number
def calc(x, c):
    return x**2 + c

# Initial value
x = 0.8
n = 0

while n < 20:
    x = calc(x, 0.15j)
    n += 1
