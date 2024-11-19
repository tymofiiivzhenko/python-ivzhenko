import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0.1, 10, 1000)

y = np.cos(x**2) / x

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$Y(x) = \frac{\cos(x^2)}{x}$", color='blue')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Лінія y = 0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Лінія x = 0
plt.title("Графік функції $Y(x) = \\frac{\\cos(x^2)}{x}$")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.legend()
plt.grid(True)
plt.show()
