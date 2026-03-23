# Bài 6:
info ={}
n = int(input("Bạn muốn nhập bao nhiêu người:"))
for i in range(n):
    name = input(f"Nhập tên người thứ {i +1}:")
    age = int(input(f"Nhập số tuổi của {name}:"))
    info[name] = age
    print(f"Đã lưu thông tin của {name} thành công")
print("\nThông tin đã lưu:")
for s, v in info.items():
    print(f"Tên:{s}, Tuổi: {v}")
avg_age = sum(info.values()) / len(info)
print("\nTuổi trung bình:",avg_age)
