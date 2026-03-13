def tuple(numbers):
    tong = sum(numbers)
    lon_nhat = max(numbers)
    nho_nhat = min(numbers)
    return tong, lon_nhat, nho_nhat
my_tuple = (90, 25, 18, 2, 11)
ket_qua = tuple(my_tuple)
print(f"Tổng: {ket_qua[0]}, Lớn nhất: {ket_qua[1]}, Nhỏ nhất: {ket_qua[2]}")
