import math as m
class Spherical:

    def __init__(self,r):
       self.radius = r
        

    def changeR(self,Radius):
       self.radius = Radius
        
    def findVolume(self):
       self.volume = 4/3 * m.pi * (self.radius**3) 
       return self.volume

    def findArea(self):
       self.area = 4 * m.pi * (self.radius**2) 
       return self.area

    def __str__(self):
       return 'Radius ={} Volumn = {} Area = {}'.format(self.radius,self.findVolume(),self.findArea())
        

r1, r2 = input("Enter R : ").split()
R1 = Spherical(int(r1))
print(type(R1))
print(dir(R1))
print(R1)
R1.changeR(int(r2))
print(R1)