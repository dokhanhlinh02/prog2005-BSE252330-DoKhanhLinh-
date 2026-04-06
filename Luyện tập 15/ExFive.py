# Bài 5:
def count_vowels(s):
    vowels = ("aeiouAEIOU")
    tong = 0
    for n in s.lower():
        if n in vowels:
            tong += 1
    return tong
a = input("Nhập một chuỗi:")
print("Số nguyên âm là:",count_vowels(a))
