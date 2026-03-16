# Bài 4:
s = input("Nhập một chuỗi: ")
hoa = thuong = chu_so = dac_biet = khoang_trang = nguyen_am = phu_am = 0
vowels = "aeiouAEIOU"
for c in s:
    if c.isupper():
        hoa += 1
    if c.islower():
        thuong += 1
    if c.isdigit():
        chu_so += 1
    if c == " ":
        khoang_trang  += 1
    if c.isalpha():
        if c.islower():
            nguyen_am += 1
        else:
            phu_am += 1
    if not c.isalnum() and c != "_":
        dac_biet += 1
print("Số chữ cái in hoa là:", hoa)
print("Số chữ cái in thường là:", thuong)
print("Số lượng chữ số là:", chu_so)
print("Số ký tụ đặc biệt là:", dac_biet)
print("Số ký tự khoảng trắng là:", khoang_trang )
print("số lượng nguyên âm là:", nguyen_am)
print("Số lượng phụ âm là:", phu_am)
