# Bài 2:
n = int(input("Nhập một số dương: "))
if n < 2:
    print("Không phải số nguyên tố")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break
    print("Nguyên tố" if is_prime else "Không phải nguyên tố")
