# Bài 14
number = float(input("Nhập một số :"))
if number < 0:
    print("Lỗi, không thể tính căn bậc hai của số âm")
else:
    square_root = number ** 0.5
    print("Căn bậc hai của số là:",square_root)
