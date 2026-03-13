# Bài 10:
code = input("Nhập mã sản phẩm: ")
name = input("Nhập tên sản phẩm: ")
price = float(input("Nhập giá sản phẩm: "))

with open("products.txt", "a", encoding="utf-8") as f:
    f.write(f"{code};{name};{price}\n")
print("Đã thêm sản phẩm vào tệp products.txt")

products = []
with open("products.txt", "r", encoding="utf-8") as f:
    for line in f:
        parts = line.strip().split(";")
        if len(parts) == 3:
            code, name, price = parts[0], parts[1], float(parts[2])
            products.append((code, name, price))
          
print("\nDanh sách sản phẩm:")
for p in products:
    print(f"{p[0]} - {p[1]} - {p[2]}")
  
products_sorted = sorted(products, key=lambda x: x[2], reverse=True)
print("\nDanh sách sản phẩm (sắp xếp theo giá giảm dần):")
for p in products_sorted:
    print(f"{p[0]} - {p[1]} - {p[2]}")
