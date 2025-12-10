class Rectangle:
    def __init__(self, width, height): 
        self.width = width
        self.height = height
    
    def __str__(self):
        return f"Rectangle width={self.width}, height={self.height}"

rect=Rectangle(10, 5)
print(rect)


