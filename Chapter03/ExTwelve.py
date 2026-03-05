# Bài 12:
m, n = map(int, input("Nhập số hàng và số cột (m n):").split())
print("Nhập ma trân A:")
A = []
for i in range(m):
    row = list(map(int, input().split()))
    A.append(row)
print("Nhập ma trán B:")
B = []
for i in range(m):
    row = list(map(int, input().split()))
    B.append(row)
C = []
for i in range(m):
    row = []
    for j in range(n):
        row. append( A[i][j] +B[i][j] )
    C.append(row)
print("Kết quả cộng hai ma trân:")
for row in C:
    print(row)
