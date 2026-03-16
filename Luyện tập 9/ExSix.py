# Bài 6:
class Product:
    def __init__(self, price):
        self._price = price
    def price(self):
        return self._price
    def price(self, value):
        if value > 0:
            self._price = value
        else:
            print("Giá phải lớn hơn 0")
    def __str__(self):
        return f"Price: {self._price}"
p = Product(212)
print(p)
