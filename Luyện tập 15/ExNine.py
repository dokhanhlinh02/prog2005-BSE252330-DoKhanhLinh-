# Bài 9:
a = input("Nhập chuỗi: ")
with open("nd.txt", "w", encoding="utf-8") as f:
    f.write(a)
print("Đã lưu vào file output.txt")
