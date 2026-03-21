# Bài 13: Yêu cầu: Nhập hai số nguyên từ bàn phím và in ra kết quả phép chia của chúng. Xử lý chia cho 0 và dữ liệu không hợp lệ.
a = int(input("Nhập số chia nguyên thứ nhất:"))
b = int(input("nhập số chia nguyên thứ hai:"))
if b == 0:
    print("Lỗi : Không thể chia cho 0")
else:
    result = a / b
    print("Kết quả phép chia là:",result)
