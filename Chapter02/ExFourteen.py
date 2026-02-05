# Bài 14:
n = int(input("Nhập số n:"))
if n < 2:
    print("Không phải số nguyên tố")
else:
    prime = True
    i = 2
    while i <= int(n**0.5):
        if n % i == 0:
            prime = False
            break
        i += 1
    print("Nguyên tố" if prime else "Không phải nguyên tố")
