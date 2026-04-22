class Shapes:
    def area(self):
        print("the area is:")
class rectangle(Shapes):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print("the area of rectangle is:",self.l*self.b)
l=int(input("enter the value of length ="))
b=int(input("enter the value of breadth="))
class square(Shapes):
    def __init__(self,s):
        self.s=s
    def area(self):
        print("the area of the square:",self.s*self.s)

r=rectangle(1,b)
r.area()
a=square(5)
a.area()

        