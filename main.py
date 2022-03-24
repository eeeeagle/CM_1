import math
import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate

"""
TASK 1
"""
print("=====================\nTASK 1\n")

J = np.ones((10, 10), dtype=float)
print("Float ones matrix J:")
print(J)

Id = np.identity(10, dtype=float)
print("\nIdentity matrix Id:")
print(Id)


"""
TASK 2
"""
print("\n=====================\nTASK 2\n")

M = np.array([[2, 1, 3, 6],
              [4, 1, 3, 3],
              [5, 2, 4, 1],
              [5, 1, 2, 2]], int)
print(M)
print("Determinant = ", np.linalg.det(M))

"""
TASK 3
"""
print("\n=====================\nTASK 3\n")

A = np.random.randint(-3, 6, (4, 4))
print("Matrix A:")
print(A)

B = np.array([[6], [4], [-5], [12]], dtype=int)
print("\nColumn vector B:")
print(B)

X = np.linalg.solve(A, B)
print("\nSolution of the AX = B:")
print(X)

"""
TASK 4
"""
print("\n=====================\nTASK 4\n")

print("Integral from -1/2 to 1/2 of 1/sqrt(1-x^2) dx")
print(integrate.quad(lambda x: (1/(math.sqrt(1 - (x * x)))), -1/2, 1/2))

"""
TASK 5
"""
print("\n=====================\nTASK 5\n")

print("Integral from 0 to +inf of cos(2x) dx - is divergent\n"
      "Integral of cos(2x) dx = arcsin(x) + C\n"
      "arcsin(x): 0 <= x <= 1"
      "Integral from 0 to 1 of cos(2x) dx")
print(integrate.quad(lambda x: (math.cos(2*x)), 0, 1))

"""
TASK 6
"""

plt.figure(figsize=(8, 5), dpi=80)
plt.suptitle("TASK 6")
ax = plt.subplot(111)

ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')

ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))

ax.text(-0.05, 2.3, "y", fontsize=15)
ax.text(6.6, -0.05, "x", fontsize=15)

X = np.linspace(-7*np.pi / 3, 7*np.pi / 3, 256, endpoint=True)
Y1 = np.sin(X + (np.pi/3))
Y2 = 2*X

plt.plot(X, Y1, color="blue", linewidth=2.5, linestyle="-", label="y = sin(x + [pi/3])")
plt.plot(X, Y2, color="red", linewidth=2.5, linestyle="-", label="y = 2x")

plt.xlim(-25*np.pi / 12, 25*np.pi / 12)
plt.xticks(np.arange(-2*np.pi, 13*np.pi / 6, np.pi / 6))

plt.ylim(-2.2, 2.2)
plt.yticks(np.arange(-2, 2.2, 0.5))

plt.legend(loc='upper left', frameon=False)
plt.grid()
plt.show()
