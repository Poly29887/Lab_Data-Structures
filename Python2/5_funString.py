class funString():

    def __init__(self,string = ""):

        ### Enter Your Code Here ###

    def __str__(self):

        ### Enter Your Code Here ###

    def size(self) :

        ### Enter Your Code Here ###

    def changeSize(self):

        ### Enter Your Code Here ###

    def reverse(self):

        ### Enter Your Code Here ###

    def deleteSame(self):

       ### Enter Your Code Here ###



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)

if str2 == "1" :    print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())