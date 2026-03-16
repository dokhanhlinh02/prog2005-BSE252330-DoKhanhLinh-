# Bài 10:
class Sinh_vien:
    def __init__(self, diem):
        self.diem = diem
    def __eq__(self, other):
        return self.diem == other.diem
sinh_vien1 = Sinh_vien(10)
sinh_vien2 = Sinh_vien(8.5)
if sinh_vien1 == sinh_vien2:
    print("Hai sinh viên có điểm bằng nhau")
else:
    print("Hai sinh viên có điểm không bằng nhau")
