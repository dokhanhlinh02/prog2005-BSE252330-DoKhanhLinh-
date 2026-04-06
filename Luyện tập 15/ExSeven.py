# Bài 7:
hoc_sinh = {
    "Nhi":9.0,
    "Trà":8.5,
    "Linh": 8.
}
def dien_trung_binh(hoc_sinh):
    tong = sum(hoc_sinh.values())
    return tong/ len(hoc_sinh)
print("Điểm trung bình :", dien_trung_binh(hoc_sinh))
