"""
class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return self.a+other.a,self.b+other.b
        #return  10+15,         20+25
p=Point(100,200)
p1=Point(150,250)
print(p+p1)

"""
#program 2-->
"""
class Point:
    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self, other):
        return Point(self.a+other.a,self.b+other.b)
       

    def __sub__(self, other):
        return Point(self.a-other.a,self.b-other.b)


    def __str__(self):
        return f'{self.a} and {self.b}'
            

    def __repr__(self):
        return f'{self.a} and {self.b}'


p=Point(100,200)
p1=Point(150,250)
#print(p+p1)
print(p-p1) 
"""


class flower:

    def __init__(self,a,b):
        self.a=a
        self.b=b

    def __add__(self,a,other):
        return flower (f'self.a+other.a,self.b+other.b')

    def __truedivision__(self,other):
                return flower(self.a-other.a,self.b-other.b)


f=flower(50,50)
f1=flower(100,100)
print(f+f1)
print(f/f1)
        

