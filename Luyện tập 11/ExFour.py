# Bài 4:
lst = [ 2, 6, 18, 22, 15]
lst.append(int(input("Nhập số cần thêm vào: ")))
s = int(input("Nhập giá trị s:"))
print("Số lần xuất hiện:", lst.count(s))
def is_prime(n):
    if n < 2:
        return False
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print("Tổng số nguyên tố:", sum(x for x in lst if is_prime(x)))
lst.sort()
print("Danh sách sau sắp xếp:",lst)
lst.clear()
print("Danh sách sau khi xóa:", lst)
