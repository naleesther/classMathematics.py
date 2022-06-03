class Circle:
   def __init__(self,radius):
       self.radius = radius

   def area(self):
       A=3.14*self.radius**2
       return A
   def circumference(self):
       C=3.14*self.radius**2
       return C

class Square:
    def __init__(self,side):
        self.side=side

    def area(self):
        A=self.side*self.side
        return A
    def perimeter(self):
        P=4*self.side
        return P
class Rectangle:
    def __init__(self,w,l):
        self.w=w
        self.l=l
    def area(self):
        A=self.w*self.l 
        return A
    def perimeter(self):
        P=2*(self.w + self.l)
        return P  
class Sphere:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        A=4*(22/7**2)  
        return A
    def volume(self):
        V=4/3*(22/7**3) 
        return V                          








