# Bài 2:
arr = ['32,45,29,45,29,20,10,33', '4,6,8,1,10,22,', '64,3,8,,2', '5,8,29', '1,2']
print("Danh sách đã sắp xếp:", arr)
def binary_search(arr, target):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left+right)//2
        if arr[mid] == target:
            return mid
        elif len(arr[mid]) > len(target):
            left = mid + 1
        else:
            right = mid - 1
    return-1
target = input("Nhập chuỗi cần tìm:")
pos = binary_search(arr, target)
if pos != -1:
    print(f"chuỗi '{target}' nằm ở vị trí {pos} trong danh sách")
else:
    print(f"chuỗi '{target}'không tồn tại trong danh sách.")
