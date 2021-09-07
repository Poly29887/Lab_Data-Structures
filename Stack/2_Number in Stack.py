class ManangeStack:
    def __init__(self,list = None):
       if list == None:
        self.items = []
       else:
        self.items = list
    def setStack(self,new):
       self.items = new
    def push(self,i) :
       print(f'Add = {i}')
       self.items.append(i)
    def pop(self):
       if self.isEmpty(): 
          print(-1)
       else:
        print(f'Pop = {self.items[-1]}')
        self.items.pop()
    def delete(self,i):
       if self.isEmpty(): 
          print(-1)
       else:
        while i in self.items:
          print(f'Delete = {i}')
          self.items.remove(i)
    def less_delete(self,i):
       temp = []
       if self.isEmpty(): 
          print(-1)
       else:
        for e in self.items:
          if e < i:
            temp.append(e)
        temp.reverse()
        for em in temp:
            self.items.remove(em)
            print(f'Delete = {em} Because {em} is less than {i}')
    def more_delete(self,i): 
       temp=[]  
       if self.isEmpty(): 
          print(-1)
       else:
        for e in self.items:
          if e > i:
            temp.append(e)
        temp.reverse()
        for em in temp:
            self.items.remove(em)
            print(f'Delete = {em} Because {em} is more than {i}')
    def isEmpty(self):
       return self.items == []
    def size(self):
       return len(self.items) 
    def __str__(self):
       return f'Value in Stack = {self.items}'
           

inp = input('Enter Input : ').split(',')
s = ManangeStack()
for e in inp:
   if e[0] == 'P':
      s.pop()
   else:
      command,value = e.split()
      if command == 'A':
         s.push(int(value))
      elif command == 'D':
         s.delete(int(value))
      elif command == 'LD':
         s.less_delete(int(value))
      elif command == 'MD':
         s.more_delete(int(value))     
print(s)
