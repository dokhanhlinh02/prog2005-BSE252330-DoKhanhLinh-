# Bài 15
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
