# Bài 15:
s = input("Nhập chuỗi muốn đảo ngược:")
# Cách 1: slicing
print("Đảo ngược bằng slicing:", s[::-1])

# Cách 2: không dùng slicing
reversed_s = ""
for ch in s:
    reversed_s = ch + reversed_s
print("Đảo ngược không dùng slicing:", reversed_s)
