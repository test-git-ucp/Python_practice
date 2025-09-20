class circle:
    def __init__(self,radius):
        self.radius=radius
    def area(self):
        
        areaa=3.14*(self.radius**2)
        return areaa
    def info(self):
        print(f"Radius of circle:{self.radius}")
        print(f"Area of circle  : {self.area()}")
        
        
t1=circle(7)

t1.info()