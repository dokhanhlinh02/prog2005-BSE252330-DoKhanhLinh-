# Bài 4:
a = int(input("Nhập điểm môn thứ nhất:"))
b = int(input("Nhập điểm môn thứ hai:"))
c = int(input("Nhập điểm môn thứ ba:"))
TB = ( a + b + c) / 2
if TB >= 8:
    print("Giỏi")
elif 6.5 <= TB <= 7.9:
    print("Khá")
elif 5.0 <= TB <= 6.4:
    print("Trung Bình")
else:
    print("Yếu")
