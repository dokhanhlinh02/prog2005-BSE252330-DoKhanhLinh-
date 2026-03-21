# Bài 6: Yêu cầu: Kiểm tra một số chẵn. Viết một hàm is_even(n) trả về True nếu n là số chẵn, ngược lại trả về False.
def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False
n = int(input("Nhập một số nguyên:"))
print(is_even(n))
