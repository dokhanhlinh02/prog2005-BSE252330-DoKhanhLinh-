# Bài 3:
def chuan_hoa(s):
    cac_tu = s.split()
    in_ra = " ".join([tu.capitalize() for tu in cac_tu])
    return in_ra
in_vao = "nguyêN VăN a"
print(chuan_hoa(in_vao))
