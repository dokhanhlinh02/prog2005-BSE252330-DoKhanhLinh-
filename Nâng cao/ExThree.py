# Bài 1:
# hình 1:
n = 4
for i in range(n):
    print(" 1 " * n)

# hình 2:
for i in range(n):
    for j in range(1, n +1):
        print(j , end = "  ")
    print()

# hình 3:
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print( j , end = "  ")
    print( )

# hình 4:
for i in range(n, 0, -1):
    for j in range(1, i +1):
        print(j, end = "  ")
    print()

# hình 5:
for i in range(1, n+1):
    if i == 1:
        print("1")
    elif i == n:
        for j in range(1, n+1):
            print(j, end=" ")
        print()
    else:
        print("1" + " " * (2*i - 3) + str(i))

# hình 6:
for i in range(n, 0, -1):
    if i == n:
        for j in range(1, n+1):
            print(j, end=" ")
        print()
    elif i == 1:
        print("1")
    else:
        print("1" + " " * (2*i - 3) + str(i))

# hình 7:
for i in range(1, n+1):
    print(" " * (n - i), end=" ")
    print((str(i) + "  ") * i)

# hình 8:
for i in range(1, n+1):
    print("  " * (n - i), end="")
    for j in range(1, i+1):
        print(j, end=" ")
    for j in range(i-1, 0, -1):
        print(j, end=" ")
    print()

# hình 9:
n = 4
for i in range(1, n+1):
    # khoảng trắng để căn giữa
    print("  " * (n - i), end="")
    if i == 1:  # dòng đầu
        print("1")
    elif i == n:  # dòng cuối: in đầy đủ đối xứng
        for j in range(1, n+1):
            print(j, end=" ")
        for j in range( n-1, 0, -1):
            print(j, end=" ")
        print()
    else:  # các dòng giữa: chỉ in số ở biên
        print("1" + "  " * (2*i - 3) + "1")
