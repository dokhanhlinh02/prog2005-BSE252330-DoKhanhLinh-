# Bài 3:
colors = ["Orange","yellow","red","blue","black"]
try:
    colors.remove("green")
except ValueError:
    print("lỗi: Màu 'green' không tồn tại trong danh sách trên")
print(f" Danh sách hiện tại: {colors}")
