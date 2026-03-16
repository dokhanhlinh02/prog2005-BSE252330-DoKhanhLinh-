# Bài 7:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    @classmethod
    def from_string(cls, s):
        name, age = s.split("-")
        return cls(name, int(age))
p = Person.from_string("linh-18")
print(p.name)
print(p.age)
