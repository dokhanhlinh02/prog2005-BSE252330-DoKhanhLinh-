# Bài 3:
n = int(input("Nhập số n:"))
a, b = 0, 1
fib = []
for _ in range(n):
    fib.append(a)
    a, b = b, a + b
print("Dãy Fibonacci:", fib)
