# Bài 12: Yêu cầu: Tính BMI (Chỉ số khối cơ thể)
#Viết một chương trình tính và hiển thị BMI:
#Nhập cân nặng (kg) và chiều cao (m)
#Công thức: BMI = weight / (height * height), sử dụng kiểu float và các toán tử số học.
#Hiển thị BMI làm tròn 2 chữ số thập phân
#Ví dụ: nếu weight = 60kg và height = 1.65m → BMI ≈ 22.04
weight = float(input("Nhập cân nặng(kg):"))
height = float(input("Nhập chiều cao(m):"))
BMI = weight / (height * height)
print("BMI của cơ thể là:",round (BMI,2))
