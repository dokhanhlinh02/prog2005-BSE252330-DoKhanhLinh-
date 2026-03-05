# Bài 9:
nums = list(map(int,input("Nhập danh sách số:").split()))
print("Các số lẻ trong danh sách là:")
for num in nums:
    if num % 2 != 0:
        print(num)
