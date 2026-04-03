# Bài 4:
class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name
    def set_name(self, name):
        self._name = name
    def get_price(self):
        return self._price
    def set_price(self, price):
        self._price = price
book1 = Book("Book 1", 30000)
print("Giá của đối tượng:", book1.get_price())
