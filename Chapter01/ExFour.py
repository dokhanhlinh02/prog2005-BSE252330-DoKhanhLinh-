# Bài 4: Yêu cầu: Hàm tính tổng hai số. Viết một hàm sum_two_numbers(a, b) trả về tổng của hai số nguyên. Gọi hàm và in ra kết quả
def sun_two_numbers(a,b):
    return a+b
number1 = int(input("Nhập số nguyên thứ nhất:"))
number2 = int(input("Nhập số nguyên thứ hai:"))
ketqua = sun_two_numbers(number1,number2)
print("Tổng hai số nguyên:",ketqua)
