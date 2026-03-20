# Bài 5:
import matplotlib.pyplot as plt
import numpy as np
x = np.linspace(0,10,100)
y1 = x**2
y2 = np.sqrt(x)
plt.figure(figsize = ( 10, 4))
# Subplot bên trái
plt.subplot(1,2,1)
plt.plot(x,y1)
plt.title("y = x^2")
plt.xlabel("x")
plt.ylabel("y")
# Subplot bên phải
plt.subplot(1,2,2)
plt.plot(x,y2)
plt.title("y = sqrt(x)")
plt.xlabel("x")
plt.ylabel("y")
plt.tight_layout()
plt.show()
