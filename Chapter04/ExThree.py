# Bài 3:
students = {"Linh": 9.4, "Hà": 8.0,"Trà": 8.7}
key = input("Nhập tên sinh viên cần kiểm tra: ")
if key in students:
    print(f"Key '{key}' tồn tại trong dictionary.")
else:
    print(f"key '{key}' không tồn tại trong dictionary.")
