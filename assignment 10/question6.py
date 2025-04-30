# The bisection method is a technique for finding solutions (roots) to equations with a single
# unknown variable. Given a polynomial function f, this code finds a root within a specified
# interval using the bisection method. It stores all intermediate values in a Numpy array and
# visualizes the root-finding process using the matplotlib/pyplot library.

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 6*x**2 + 11*x - 6  # Example polynomial function

def bisection_method(func, a, b, tol=1e-5, max_iter=100):
    if func(a) * func(b) >= 0:
        print("The function must have opposite signs at a and b. No root found in the given interval.")
        return None, np.array([])
    
    iterations = []
    for _ in range(max_iter):
        c = (a + b) / 2
        iterations.append(c)
        if abs(func(c)) < tol or abs(b - a) < tol:  # Check for convergence
            break
        if func(a) * func(c) < 0:
            b = c
        else:
            a = c
    return c, np.array(iterations)
# Define the interval [a, b]
a, b = 1, 3

# Perform the bisection method
root, updates = bisection_method(f, a, b)

# Plot the root-finding process
x_vals = np.linspace(a, b, 500)
y_vals = f(x_vals)

plt.plot(x_vals, y_vals, label="f(x)")
plt.axhline(0, color='black', linewidth=0.8, linestyle='--')
plt.scatter(updates, f(updates), color='red', label="Iterations")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid()
plt.show()

print(f"Root found: {root}")