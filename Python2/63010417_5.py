class funString():
    
    def __init__(self,string = ""):
      self.string = string
      self.list_str = list(self.string)
      self.big = ['A','B','C','D','E','F','G','H','I','J',
                  'K','L','M','N','O','P','Q','R','S','T',
                  'U','V','W','X','Y','Z']
      self.small = ['a','b','c','d','e','f','g','h','i','j',
                    'k','l','m','n','o','p','q','r','s','t',
                    'u','v','w','x','y','z']  

    def __str__(self):
      return self.string
      

    def size(self) :
      return len(self.string)
        

    def changeSize(self):
      i=0
      for i in range (len(self.list_str)):
        if self.list_str[i] in self.big :
          n = self.big.index(self.list_str[i]) 
          self.list_str[i] = self.small[n] 
        elif self.list_str[i] in self.small :    
          n = self.small.index(self.list_str[i]) 
          self.list_str[i] = self.big[n] 
        i+=1
      self.string = ''.join(self.list_str)
      return self.string 
        

    def reverse(self):
       self.rev=''
       for i in range(len(self.list_str)-1,-1,-1):
        self.rev += self.list_str[i]
       return self.rev 
        

    def deleteSame(self):
       check = []
       for elem in self.list_str:
           if elem not in check:
               check.append(elem)
       self.string=''.join(check)
       return self.string
      



str1,str2 = input("Enter String and Number of Function : ").split()

res = funString(str1)
if str2 == "1" :  print(res.size())

elif str2 == "2":  print(res.changeSize())

elif str2 == "3" : print(res.reverse())

elif str2 == "4" : print(res.deleteSame())

