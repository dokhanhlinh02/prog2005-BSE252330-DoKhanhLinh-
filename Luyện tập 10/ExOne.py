# Bài 1:
path = "d:\\music\\muabui.mp3"
def lay_ten_file(path):
    return path.split("\\")[-1]
def lay_ten_khong_duoi(path):
    ten_file = path.split("\\")[-1]
    return ten_file.split(".")[0]
print(lay_ten_file(path))
print(lay_ten_khong_duoi(path))
