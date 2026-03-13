# Bài 6:
import math
s = input("Nhập chuỗi số (vd: 5; 7; 8; -2; 8; 11; 13; 9; 10):" )
numb = [int(x.strip()) for x in s.split(" ")]
print("Các số:")
for num in numb:
    print(num)
chan = sum(1 for num in numb if num % 2 == 0)
am = sum(1 for num in numb if num < 0)
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True
nguyento = sum(1 for num in numb if is_prime(num))
TB = sum(numb) / len(numb)
print("Số chẵn là:", chan)
print("Số âm là:", am)
print("Số nguyên tố là:", nguyento)
print("Giá trị trung bình là:", TB)
