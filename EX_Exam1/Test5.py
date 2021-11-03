class MyInt:
    def __init__(self,n):
        self.number = n

    def toRoman(self):
        s=""
        x=self.number
        while x >0:
            if x >= 1000:
                s+="M"
                x-=1000
            elif x >= 900:
                s+="CM"
                x-=900
            elif x >= 500:
                s+="D"
                x-=500
            elif x >= 400:
                s+="CD"
                x-=400
            elif x >= 100:
                s+="C"
                x-=100
            elif x >= 90:
                s+="XC"
                x-=90
            elif x >= 50:
                s+="L"
                x-=50
            elif x >= 40:
                s+="XL"
                x-=40
            elif x >= 10:
                s+="X"
                x-=10
            elif x >= 9:
                s+="IX"
                x-=9
            elif x >= 5:
                s+="V"
                x-=5
            elif x >= 4:
                s+="IV"
                x-=4
            elif x >= 1:
                s+="I"
                x-=1
        return str(self.number) +" convert to Roman : "+s
    
    def __add__(self,other):
        return str(self.number) + " + "+str(other.number)+" = "+str(int((self.number+other.number)+((self.number+other.number)/2)))



print(" *** class MyInt ***")
inp = input("Enter 2 number : ").split()
a = MyInt(int(inp[0]))
b = MyInt(int(inp[1]))
print(a.toRoman())
print(b.toRoman())
print(a+b)
