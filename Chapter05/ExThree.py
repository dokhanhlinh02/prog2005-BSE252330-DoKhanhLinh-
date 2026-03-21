# Bài 3:
import matplotlib.pyplot as plt
sizes = [30, 25, 15, 20, 10]
labels = ("A","B","C","D","E")
colors = ["gold", "lightblue", "lightgreen", "pink", "orange"]
plt.figure(figsize = (6, 6))
plt. pie(sizes, labels = labels, autopct ="%1.1f%%", colors = colors, startangle = 90)
plt.title("Tỷ lệ doanh số các sản phẩm")
plt.show()
