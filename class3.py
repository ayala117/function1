#Define a class named Rectangle which inherits from Shape class from task 2. Class instance can be constructed by a length and width. The Rectangle class has a method which can compute the area.

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width

    def area(self):
        self.area_value = self.length * self.width
        print(f"Area of Rectangle: {self.area_value}")

# Example usage
rect = Rectangle(4, 5)
rect.area()  
# Output: Area of Rectangle: 20
