# Bài 5:
books = [
    ("Book 1", 300000),
    ("Book 2", 500000),
    ("Book 3", 100000)
]
with open("books.txt", "w", encoding="utf-8") as f:
    f.write("Book 1;30000\n")
    f.write("Book 2;50000\n")
    f.write("Book 3;100000\n")
    f.write("Tong;180000\n")
