# Bài 9:
def input_matrix(rows, cols, name):
    matrix = []
    for i in range(rows):
        row = input(f"Nhập hàng {i+1} của ma trận {name} (cách nhau bởi khoảng trắng): ").split()
        if not row or len(row) != cols:
            raise ValueError(" Dữ liệu không hợp lệ! Vui lòng nhập đủ số phần tử.")
        matrix.append(list(map(int, row)))
    return matrix
rows = int(input("Nhập số hàng: "))
cols = int(input("Nhập số cột: "))
print("Nhập ma trận A:")
A = input_matrix(rows, cols, "A")
print("Nhập ma trận B:")
B = input_matrix(rows, cols, "B")
C = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
print("\nKết quả cộng ma trận:")
for row in C:
    print(row)
