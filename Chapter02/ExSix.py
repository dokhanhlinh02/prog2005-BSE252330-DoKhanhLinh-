# Bài 6:
def factorial (n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n-1)
n = input(input("Nhập số:"))
print("Giai thừa:", factorial(n))
