class translator:
    def __init__(self):
      self.rom2dec = {'M':1000,'D':500,'C':100,'L':50,'X':10,'V':5,'I':1}
      self.dec2rom = {1000:'M',900:'CM',500:'D',400:'CD',100:'C',90:'XC',50:'L',40:'XL',10:'X',9:'IX',5:'V',4:'IV',1:'I'}
      self.dec = [1000,900,500,400,100,90,50,40,10,9,5,4,1]
      self.rom = ['M','CM','D','CD','C','XC','L','XL','X','IX','V','IV','I']
      
    def deciToRoman(self, num):
      roman=''
      while num>0:
        for x in self.dec:
          for i in range(num//x):
            roman += self.dec2rom[x]
            num -= x
      return roman
      
    def romanToDeci(self, s):
     dec=0
     for i in range(len(s)-1):
      left_s = self.rom2dec[s[i]]
      right_s = self.rom2dec[s[i+1]]
      if left_s < right_s:
       dec -= left_s
      else :
       dec += left_s
     dec += self.rom2dec[s[-1]]

     return dec
      

num = int(input("Enter number to translate : "))

print(translator().deciToRoman(num))
print(translator().romanToDeci(translator().deciToRoman(num)))
