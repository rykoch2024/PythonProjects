# The following code is from freecodecamp.org
# Path: The Scientific Computing with Python.
# Project: Build a Polygon Area Calculator Project


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, newWidth):
        self.width = newWidth

    def set_height(self, newHeight):
        self.height = newHeight

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        returnPic = ''
        
        if self.height > 50 or self.width > 50:
            return f'Too big for picture.'
        for i in range(self.height):
            for j in range(self.width):
                returnPic += '*'
            returnPic += '\n'
        
        return returnPic

    def get_amount_inside(self, other):
        remainingWidth = self.width
        remainingHeight = self.height
        across = 0
        tall = 0
        
        while remainingWidth >= other.width:
            across += 1
            remainingWidth -= other.width
        while remainingHeight >= other.height:
            tall += 1
            remainingHeight -= other.height

        return across * tall
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
    
    def __str__(self):
        return f'Square(side={self.height})'
    
    def set_side(self, newSide):
        super().set_height(newSide)
        super().set_width(newSide)

    def set_height(self, newHeight):
        super().set_height(newHeight)
        super().set_width(newHeight)

    def set_width(self, newWidth):
        super().set_height(newWidth)
        super().set_width(newWidth)
    
mySquare = Square(5)
print(mySquare)
mySquare.set_side(newSide=7)
print(mySquare)

print(Rectangle(15,10).get_amount_inside(Square(5)))