# Bài 7:
import csv
import pyautogui
name = input("Nhập tên nhân viên:")
age = int(input("Nhập tuổi:"))
emp_id = input("Nhập ID:")
with open("Nhanvien.txt", "w", encoding="utf-8") as file:
    file.write(f"Tên:{name}, Tuổi:{age}, ID: {emp_id}")
with open("Nhanvien.csv", "w", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Tên","Tuổi","ID"])
    writer.writerow([name,age,emp_id])
print("Đã lưu thông tin vào Nhanvien.txt và Nhanvien.csv thành công ")
screenshot = pyautogui.screenshot()
screenshot.save("Nhanvien.png")
print("Đã chụp ảnh màn hình và lưu vào Nhanvien.png")
