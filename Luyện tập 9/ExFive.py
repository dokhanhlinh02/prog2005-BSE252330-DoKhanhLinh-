# Bài 5:
class User:
    def __init__(self, id):
        self.id = id
    def id(self):
        return self._id
u = User(212)
print("User id:", u.id)
