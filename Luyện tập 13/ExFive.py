# Bài 5:
class Flower:
    def __init__(self, color):
        self._color = color    
    def get_color(self):
        return self._color    
    def set_color(self, color):
        self._color = color
hoa = Flower("Red")
print("Màu ban đầu:", hoa.get_color())
hoa.set_color("Yellow")
print("Màu sau khi đổi:", hoa.get_color())
