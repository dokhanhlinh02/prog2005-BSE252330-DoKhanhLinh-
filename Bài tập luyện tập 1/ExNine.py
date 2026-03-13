class Student:
    def __init__(self, name, score):
        if 0 <= score <= 10:
            self.name = name
            self.score = score
        else:
            raise ValueError("Điểm phải nằm trong khoảng 0–10")
    def display(self):
        print(f"Sinh viên {self.name} có điểm là {self.score}")
s1 = Student("Nhi", 7)
s2 = Student("Trà", 8.6)
s1.display()
s2.display()
