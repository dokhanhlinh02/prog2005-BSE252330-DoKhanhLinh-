# Bài 5:
my_dict = {
    "name": "Linh",
    "age": 18,
    "city": "Hà Nội"
}
key = input("Nhập key cần kiểm tra: ")
if key in my_dict:
    print(f"Key '{key}' tồn tại trong dictionary với giá trị: {my_dict[key]}")
else:
    print(f"Key '{key}' không tồn tại trong dictionary.")
