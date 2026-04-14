# Bài 2:
# hình 1:
n = 4
for i in range(n):
    for j in range(n):
        print("*", end = "  ")
    print()

# hình 2:
for i in range(n + 1):
    for j in range(i):
        print("*", end = "  ")
    print()

# hình 3:
for i in range(n, 0, -1):
    for i in range(i):
        print("*", end = "  ")
    print()

# hình 4:
for i in range(1, n+1):
    print("   " * (n - i), end = " ")
    print(" * " * i)

# hình 5:
for i in range(1, n+1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("*" + "  " * (i-2) + " *")

# hình 6:
for i in range(n, 0, -1):
    if i == 1 or i == n:
        print("* " * i)
    else:
        print("*" + "  " * (i-2) + " *")
# hình 7:
n = 4
for i in range(1, n+1):
    print("  " * (n - i), end="")
    if i == 1:
        print("*")
    elif i == n:
        print("* " * i)
    else:
        print("*" + " " * (2*i - 3) + "*")

# hình 8:
for i in range(1, n+1):
    print(" " * (n - i), end = "  ")
    print(" * " * i)

# hình 9:
for i in range(1, n+1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (n - i) + "*" + "  " * (i-2) + " *")

# hình 10:
for i in range(n, 0, -1):
    if i == 1 or i == n:
        print(" " * (n - i) + "* " * i)
    else:
        print(" " * (n - i) + "*" + "  " * (i-2) + " *")
