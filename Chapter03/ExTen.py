# Bài 10:
nums = list(map(int,input("Nhập danh sách số:").split()))
even_sum = 0
print("Các số chẵn trong danh sách là:")
for num in nums:
    if num % 2 == 0:
        print(num)
        even_sum += num
print("Tổng các số chẵn:", even_sum)
