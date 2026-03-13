# Bài 10:
ma = input("Nhập mã sản phẩm: ")
ten = input("Nhập tên sản phẩm: ")
gia = float(input("Nhập giá sản phẩm: "))
s = open("products.txt","a",encoding="utf-8")
line = ma + "," + ten + "," + str(ten) + "\n"
s.write(line)
s.close()
print("Đã thêm sản phẩm vào tệp products.txt")
