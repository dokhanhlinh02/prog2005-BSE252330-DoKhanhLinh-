# Bài 3:
nums = list(map(int,input("Nhập danh sách số, cách nhau bởi khoảng trắng:"). split()))
evens = [n for n in nums if n % 2 == 0]
print("Các số chẵn :", evens)
print("Tổng các số chẵn:",sum(evens))
