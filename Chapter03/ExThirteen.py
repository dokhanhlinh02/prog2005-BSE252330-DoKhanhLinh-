# Bài 13:
s = input("Nhập chuỗi cẫn kiểm tra:").lower()
s = s.replace (" ", " ")
if s == s[:: -1]:
    print("Đây là chuỗi đối xứng!")
else:
    print("Đây không phải chuỗi dối xứng")
