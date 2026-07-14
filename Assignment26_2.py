class Circle:
    PI=3.14
    
    def __init__(self):
        self.Radius=0.0
        self.Area=0.0
        self.Circumference=0.0
        

    def Accept(self):
        self.Radius = float(input("Enter Radius : "))

    def Calculatearea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def Calculatecircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius :", self.Radius)
        print("Area :", self.Area)
        print("Circumference :", self.Circumference)
        
        
obj1=Circle()
obj1.Accept()
obj1.Calculatearea()
obj1.Calculatecircumference()
obj1.Display()

obj2=Circle()
obj2.Accept()
obj2.Calculatearea()
obj2.Calculatecircumference()
obj2.Display()







        
    
