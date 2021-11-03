from functools import lru_cache


class Myint:
  def __init__(self,num):
    self.num = num
    self.l_primeToNum = []
    self.p = 0

  def showNumber(self) :
    return self.num

  def isPrime(self):
    if self.checkPrime(self.num): return True
    else : return False

  def checkPrime(self,n):
    if n <= 1:
      return False
    for i in range(2,n): 
      if n % i == 0:
        return False
    return True  

  def showPrime(self):
    output = ''
    if self.num <= 1:
      output += '!!!A prime number is a natural number greater than 1'
    else:
      for j in range(2,self.num+1):
        if self.checkPrime(j):
          self.l_primeToNum.append(str(j))
      output = ' '.join(self.l_primeToNum)
    return output
  def __sub__(self) :
    pass


print(' *** class MyInt ***')
inp1,inp2 = input('Enter 2 number : ').split()

num1 = Myint(int(inp1))
num2 = Myint(int(inp2))
print(f'{num1.showNumber()} isPrime : {num1.isPrime()}')
print(f'{num2.showNumber()} isPrime : {num2.isPrime()}')

print(f'Prime number between 2 and {num1.showNumber()} : {num1.showPrime()}')
print(f'Prime number between 2 and {num2.showNumber()} : {num2.showPrime()}')

ans = int(num1.showNumber() - round(num2.showNumber()/2))
print('{} - {} = {}'.format(num1.showNumber(),num2.showNumber(),ans))