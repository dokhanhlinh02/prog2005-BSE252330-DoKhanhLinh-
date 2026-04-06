# Bài 8:
class Product:
    def __init__(self, price=0):
        self._price = price
    def get_price(self):
        return self._price
    def set_price(self, value):
        if value < 0:
            raise ValueError("Giá không được nhỏ hơn 0")
        self._price = value
n = Product()
n.set_price(10)
print("Giá sản phẩm:", n.get_price())
