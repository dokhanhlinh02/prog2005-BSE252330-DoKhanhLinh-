# Bài 3:
a = []
n = int(input('Nhập: '))
for i in range(n):
    a.append(int(input()))
tong = 0
for x in a:
    if x % 2 !=0:
        print (x)
        tong += 1
print('lẻ', tong)
for x in a:
    if x > 1:
        check = True
        for j in range(2, x):
            if x % j == 0:
                check = False
        if check:
            print(x)
