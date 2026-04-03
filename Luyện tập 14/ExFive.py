# Bài 5:
class Book:
    def __init__(self, name, price):
        self._name = name
        self._price = price
    def get_name(self):
        return self._name
    def get_price(self):
        return self._price
books = [
    Book("Book 1", 30000)
]
tong = sum(book.get_price() for book in books)
with open("books.txt", "w", encoding="utf-8") as f:
    for book in books:
        f.write(f"{book.get_name()};{book.get_price()}\n")
    f.write(f"Tong;{tong}\n")
