class Shape:
    def area(self):
        print("Area of shapes is in subclasses")
        
class circle(Shape):
    def cir(self,radius):
        self.radius=radius
    def area(self):
        cirarea=3.14*self.radius*2
        print(f'area of circle is :{cirarea}')
        
class rectangle(Shape):
    def rec(self,length,breadth):
        self.length=length
        self.breadth=breadth
    def area(self):
        recarea=self.length*self.breadth
        print(f'Area of Rectangle is:{recarea}')
def areas_of_shapes(area_sh):
    return({area_sh.area()})
cicle1=circle()
rectangle1=rectangle()

cicle1.cir(5)
rectangle1.rec(6,3)
areas_of_shapes(cicle1)
areas_of_shapes(rectangle1)
