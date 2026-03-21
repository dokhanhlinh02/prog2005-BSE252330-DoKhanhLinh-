# Bài 9: Yêu cầu: Kiểm tra đầu vào tuổi. Yêu cầu người dùng nhập tuổi. Kiểm tra xem tuổi có nằm trong khoảng 1 đến 120 không. In ra thông báo phù hợp
age = int(input("Nhập tuổi:"))
if age >= 1 and age <= 120:
    print("Tuổi hợp lệ")
else:
    print("Tuổi không hợp lệ")
