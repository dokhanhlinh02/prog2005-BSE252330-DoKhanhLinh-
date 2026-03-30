# Bài 3:
i = 1
tong = 0
print("Các số lẻ từ 1 đến 30:")
while i <= 30:
    if i % 2 != 0:
        print(i, end=" ")
        tong += i
    i += 1
print("\nTổng các số lẻ từ 1 đến 30 là:", tong)
