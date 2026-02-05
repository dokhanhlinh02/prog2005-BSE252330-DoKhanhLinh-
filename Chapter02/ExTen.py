# Bài 10 :
def tong(n):
    if n == 1:
        retuen 1
    return n + tong(n-1)
n = int(input("Nhập số n:"))
print("Tổng từ 1 đến n:", tong(n))
