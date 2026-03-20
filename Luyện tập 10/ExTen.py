# Bài 8:
def bubble_sort_string():
    arr = []
    print("Nhập vào 5 chuỗi:")
    for i in range(5):
        s = input(f"chuỗi{i+1}: ")
        arr.append(s)
    n = len(arr)
    for i in range(n):
        swappend = False
        for j in range(0, n - 1 - i):
            if len(arr[j]) < len(arr[j + 1]):
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swappend = True
                print(f"Tráo đổi: {arr}")
        if not swappend:
            break
    print("kết quả cuối cùng(giảm dần theo độ dài):")
    for s in arr:
        print(f"'{s}'(độ dài:{len(s)})")
bubble_sort_string()
