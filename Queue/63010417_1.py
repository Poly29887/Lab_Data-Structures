class Queue:
    def __init__(self,list=None):
      if list == None:
       self.items = []
      else:
        self.items = list
    def enQueue(self,i):
      self.items.append(i)
    def deQueue(self):
      self.items.pop(0)
    def isEmpty(self):
      return self.items == []
    def size(self):
      return len(self.items)
    def getValue(self,i):
      return self.items[0]
    def __str__(self):
      output = ""
      if self.isEmpty():
       output += "Empty"
      else :
        for e in self.items:
          output += e + " "
      return output


inp = input('Enter Input : ').split(',')
q = Queue()
i = 0

for e in inp:
  cm = e[0]
  if cm == 'E':
   x,value = e.split()
   q.enQueue(value)
   print(q.size())
  elif cm == 'D':
    if q.isEmpty(): print(-1)
    else: 
      print(q.getValue(0) + ' 0')
      q.deQueue()
print(q)