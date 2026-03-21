# Bài 14: Yêu cầu: Nhập một số và tính căn bậc hai của nó. Nếu số nhập vào âm, hiển thị thông báo lỗi.
number = float(input("Nhập một số :"))
if number < 0:
    print("Lỗi, không thể tính căn bậc hai của số âm")
else:
    square_root = number ** 0.5
    print("Căn bậc hai của số là:",square_root)
