# Bài 11:
class sinh_vien:
    count = 0
    def __init__(self, name):
        self.name = name
        sinh_vien.count += 1
    @classmethod
    def dem_so_doi_tuong(cls):
        print("Số đối tượng đã tạo:", cls.count)
sinh_vien1 = sinh_vien("Nhi")
sinh_vien2 = sinh_vien("Trà")
sinh_vien3 = sinh_vien("Linh")
sinh_vien1.dem_so_doi_tuong()
