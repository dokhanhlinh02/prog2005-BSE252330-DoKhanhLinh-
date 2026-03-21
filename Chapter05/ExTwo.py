# Bài 2:
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(-5,5,100)
y1 = x**2
y2 = x**3
plt.figure(figsize=(6,4))
plt.plot(x, y1, color = "blue", label ="y = x^2")
plt.plot(x, y2, color = "red", label ="y = x^3")
plt.title("Đồ thị hàm số y = x^2 và y = x^3")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid(True)
plt.show()
