# Bài 3:
def giaithua(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * giaithua(n - 1)
so = int(input("Nhập một số: "))
print(f"Giai thừa của {so} là {giaithua(so)}")
