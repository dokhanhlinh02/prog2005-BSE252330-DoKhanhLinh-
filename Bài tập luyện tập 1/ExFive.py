# Bài 5:
import random
M = int(input("Nhập số hàng M: "))
N = int(input("Nhập số cột N: "))
ma_tran = []
for i in range(M):
    row = []
    for j in range(N):
        row.append(random.randint(0, 100))
    ma_tran.append(row)
print("Ma trận vừa tạo:")
for row in ma_tran:
    print(row)
  
row_index = int(input("Nhập số hàng muốn hiển thị : "))
print("Hàng", row_index, ":", ma_tran[row_index])

col_index = int(input("Nhập số cột muốn hiển thị : "))
column = [ma_tran[i][col_index] for i in range(M)]

print("Cột", col_index, ":", column)
max_val = max(max(row) for row in ma_tran)
print("Giá trị lớn nhất trong ma trận:", max_val)
