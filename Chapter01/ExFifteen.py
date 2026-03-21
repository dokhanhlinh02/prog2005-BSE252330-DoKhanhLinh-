# Bài 15: Yêu cầu: Nhập thông tin 3 sinh viên (Tên và điểm 3 môn - Toán, Lý, Hóa). In ra tên sinh viên, và điểm trung bình tương ứng.
for i in range(1, 4):
    print("Sinh viên",i)
    name = input("Nhập tên sinh viên:")
    math = float(input("Nhập điểm toán:"))
    physics = float(input("Nhập điểm lý:"))
    chemsitry = float(input("Nhập điểm hóa:"))
    average =(math + physics + chemsitry)/3
    print("Tên học sinh:",name)
    print("Điểm trung bình của ba môn:",average)
    print("--------------------------")
