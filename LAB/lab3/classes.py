#1
class MyString:
    def getString(self):
        self.input = input()
    
    def printSting(self):
        print(self.input.upper())
        
#2
class Shape:
    def area(self):
        return 0
    
class Square(Shape):
    def __init__(self, length):
        self.length = length
        
    def area(self):
        return self.length ** 2

#3
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width
        
    def area(self):
        return self.length * self.width
    
#4
import math 

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def show(self):
        print(self.x, self.y)
        
    def move(self, kx, ky):
        self.x += kx
        self.y += ky
        
    def dist(self, c):
        return math.sqrt((self.x - c.x) ** 2 + (self.y - c.y) ** 2)
    
#5
