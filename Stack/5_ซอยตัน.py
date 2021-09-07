class Stack:
    def __init__(self,limit,list = None):
       if list == None:
        self.items = []
       else:
        self.items = list
       self.limit = limit
    def push(self,i) :
       self.items.append(i)
    def pop(self,i):
       self.items.pop(i)
    def arriveCar(self,car):
       if self.isFull():
          print(f'car {car} cannot arrive : Soi Full')
       elif self.isInStack(car):
          print(f'car {car} already in soi')
       else:
          print(f'car {car} arrive! : Add Car {car}')
          self.push(car)
    def departCar(self,car):
       if self.isEmpty() :
          print(f'car {car} cannot depart : Soi Empty')
       elif not self.isInStack(car):
          print(f'car {car} cannot depart : Dont Have Car {car}')
       else:
          tail = self.size()-1
          for i in range(tail,-1,-1):
             if self.items[i] == car:
                self.pop(i)
                break
          print(f'car {car} depart ! : Car {car} was remove')
    def isEmpty(self):
       return self.items == []
    def size(self):
       return len(self.items)
    def isFull(self):
       if self.size() == self.limit:
          return True
       else:
          return False
    def isInStack(self,car):
       if car in self.items:
          return True
       else:
          return False
    def __str__(self):
       output = '['
       tail = self.size()-1
       if not self.isEmpty():
        for i in range (len(self.items)):
          output += self.items[i]
          if i == tail: break
          output += ', '
       output += ']' 
       return output

   


print("******** Parking Lot ********")

max,soi,o,n = input("Enter max of car,car in soi,operation : ").split()
s = Stack(int(max))

if soi != '0':
 car_soi = []
 car_soi = soi.split(',')
 for e in car_soi:
   if s.isFull():
      print('car 5 cannot arrive : Soi Full')
      break
   s.push(e)

if o == 'arrive':
   s.arriveCar(n)
elif o == 'depart':
   s.departCar(n)

print(s)
 

