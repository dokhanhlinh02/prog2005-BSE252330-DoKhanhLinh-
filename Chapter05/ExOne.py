# Bài 1:
import matplotlib.pyplot as plt
labels = ["Xuất sắc", "Giỏi", "Trung bình", "Yếu", "Kém"]
values = [6, 10, 12, 4, 1]
plt.figure(figsize = (6, 4))
plt.bar(labels, values, color = "pink")
plt.title("Kết quả học tập của lớp")
plt.xlabel("Xếp loại")
plt.ylabel("Số học sinh")
plt.show()
