class Stack:
    def __init__(self,list = None):
       if list == None:
        self.items = []
       else:
        self.items = list
    def push(self,i) :
       self.items.append(i)
    def canSee(self,height):
       if self.isEmpty():
          self.push(height)
          
       else:
        tail = self.size()-1
        for i in range(tail,-1,-1):
          if height >= self.items[i]:
             self.pop()
          
        self.push(height)

    def pop(self):
       self.items.pop()
    def isEmpty(self):
       return self.items == []
    def size(self):
       return len(self.items)
    def top(self):
       return self.items[-1]

s = Stack()

inp = input('Enter Input : ').split(',')
for e in inp:
   if len(e)==1:
      print(s.size())
   else :
      x,height = e.split()
      s.canSee(int(height))
       