# Bài 2:
ds =[]
for i in range(5):
    ten = input(f"Nhập tên thứ {i+1}:")
    ds.append(ten)
print("Danh sách tên người nhập là:", ds)
del ds[1]
print("Danh sách sau khi xóa vị trí thứ 2 là:", ds)
