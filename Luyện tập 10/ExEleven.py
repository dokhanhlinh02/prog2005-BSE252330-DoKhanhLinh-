# Bài 11:
while True:
    print("\n===== MENU =====")
    print("1. Test class (Bài 9)")
    print("2. Bubble sort (Bài 10)")
    print("0. Thoát")
    chon = input("Chọn: ")
    if chon == "1":
        n1 = Nguoi("Nhi", 18)
        print(n1)
        print(n1.xin_chao())
    elif chon == "2":
        arr = []
        for i in range(5):
            arr.append(input(f"Nhập chuỗi {i+1}: "))
        for i in range(len(arr)):
            for j in range(len(arr) - i - 1):
                if len(arr[j]) < len(arr[j + 1]):
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
            print(f"Bước {i+1}: {arr}")
    elif chon == "0":
        print("Thoát chương trình")
        break
    else:
        print("Chọn sai!")
