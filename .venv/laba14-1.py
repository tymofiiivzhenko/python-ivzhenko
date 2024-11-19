import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-3, 3, 1000)

y = 15 * np.sin(10 * x) * np.cos(3 * x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, label=r"$Y(x) = 15 \sin(10x) \cos(3x)$", color='blue')
plt.axhline(0, color='black', linewidth=0.5, linestyle='--')  # Лінія y = 0
plt.axvline(0, color='black', linewidth=0.5, linestyle='--')  # Лінія x = 0
plt.title("Графік функції $Y(x) = 15*sin(10*x)*cos(3*x)$")
plt.xlabel("x")
plt.ylabel("Y(x)")
plt.legend()
plt.grid(True)
plt.show()
