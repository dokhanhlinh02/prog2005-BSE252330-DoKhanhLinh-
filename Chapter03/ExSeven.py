# Bài 7:
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1
nums = list(map(int,input("nhập danh sách số:").split()))
target = int(input("Nhập số cần tìm:"))
index = linear_search(nums, target)
if index != -1:
    print(f"Số {target} nằm ở vị trí {index}")
else:
    print(f"Không tìm thấy số {target}")
