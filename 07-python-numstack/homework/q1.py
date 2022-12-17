import time
import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp

"""
The program automatically generates a linear equation system with random coefficients and different sizes.
Solves each of the systems using the libraries: numpy and cvxpy.
Compares the two libraries and plots a graph of the runtime as a function of system size.

Results: It can be seen that the cvxpy library becomes slower compared to the numpy library as the size of the equation increases.
It seems that numpy's runtime increases linearly, while cvxpy's runtime increases exponentially.
"""

import time
import matplotlib.pyplot as plt
import numpy as np
import cvxpy as cp

# Solve system of equations using numpy and cvxpy and record the running time
sizes = []
times_np = []
times_cp = []
for size in range(1, 1000, 100):
    m, n = size, size

    # Generate random equations
    np.random.seed(0)
    A = np.random.randn(m, n) # Coefficients
    b = np.random.randn(m) # Result

    # Solve using numpy
    start = time.perf_counter()
    x_np = np.linalg.solve(A, b)
    end = time.perf_counter()
    times_np.append(end - start)

    # Solve using cvxpy
    x = cp.Variable(n)
    objective = cp.Minimize(0)
    constraints = [A @ x == b]
    prob = cp.Problem(objective, constraints)

    start = time.perf_counter()
    prob.solve()
    end = time.perf_counter()
    times_cp.append(end - start)

    sizes.append(size)

# Plot the running time as a function of the size of the system of equations
plt.plot(sizes, times_np, label="numpy")
plt.plot(sizes, times_cp, label="cvxpy")
plt.xlabel("Size of system of equations")
plt.ylabel("Running time (seconds)")
plt.legend()
plt.show()
