# Bài 3: Yêu cầu: Thực hiện các phép toán cơ bản với hai số. Nhập hai số nguyên từ người dùng. Tính và in ra tổng, hiệu, tích và thương của chúng
a = int(input("Số nguyên thứ nhất:"))
b = int(input("Số ngyên thứ hai:"))
tong = a + b
hieu = a - b
tich = a * b
thuong = a / b
if b != 0:
  thuong = a / b
else:
  thuong = "Không thể chia cho 0"
print("Tổng:",tong)
print("Hiệu:",hieu)
print("Tích:",tich)
print("Thương:",thuong)
