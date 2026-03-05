# Bài 6:
def bubble_sort(arr):
    n = len (arr)
    swaps = 0
    for i in range (n):
        for j in range (0, n - i - 1):
            if arr[j] > arr [j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swaps += 1
    return arr, swaps
nums = list(map(int,input("Nhập danh sách số nguyên:").split()))
sorted_numbs, swaps = bubble_sort(nums)
print("Danh sách sau khi sắp xếp:", sorted_numbs)
print("Số lần hoán đổi:", swaps)
