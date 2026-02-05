# Bài 9:
n = input("Nhập số nguyên dương 5 chữ số:")
if len(n)== 5 and n.isdigit():
    print("Nhập số lớn nhất:",max(n))
else:
    print("Không hợp lệ!")
