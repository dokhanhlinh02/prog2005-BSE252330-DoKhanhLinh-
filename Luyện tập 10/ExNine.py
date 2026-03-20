# Bài 9:
class Nguoi:
    def __init__(self, ten, tuoi):
        self.ten = ten
        self.set_tuoi(tuoi)
    def get_ten(self):
        return self.ten
    def set_tuoi(self, tuoi):
        if tuoi < 0:
            raise ValueError("Tuổi không hợp lệ!")
        self.tuoi = tuoi
    def get_tuoi(self):
        return self.tuoi
    # __str__
    def __str__(self):
        return f"Tên: {self.ten}, Tuổi: {self.tuoi}"
    def xin_chao(self):
        return f"Xin chào, tôi là {self.ten}"
    @classmethod
    def mo_ta(cls):
        return "Đây là class người"
    @staticmethod
    def thong_tin():
        return "Static method ví dụ"
    def __eq__(self, other):
        return self.ten == other.ten and self.tuoi == other.tuoi
class SinhVien(Nguoi):
    def __init__(self, ten, tuoi, mssv):
        super().__init__(ten, tuoi)
        self.set_mssv(mssv)
    def set_mssv(self, mssv):
        try:
            if len(mssv) == 0:
                raise ValueError
            self.mssv = mssv
        except ValueError:
            print("MSSV không hợp lệ!")

    def __str__(self):
        return f"{super().__str__()}, MSSV: {self.mssv}"
n1 = Nguoi("Nhi", 18)
n2 = Nguoi("Trà",19)
print(n1)
print(n1.xin_chao())
print(Nguoi.mo_ta())
print(Nguoi.thong_tin())
print("So sánh:", n1 == n2)
sv = SinhVien("Linh", 20, "SV002")
print(sv)
