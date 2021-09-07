class Queue:
    def __init__(self):
      self.items = list()
    def enQueue(self,emp):
      self.items.append(emp)

    def insertQueue(self,emp):
      if self.haveDepartment(emp[0]):
        tail = len(self.items)-1
        for i in range(tail,-1,-1):
         if self.items[i][0] == emp[0]:
          self.items.insert(i+1,emp)
          break
      else:
        self.enQueue(emp)
    def haveDepartment(self,d):
      for e in self.items:
        if d == e[0]:
          return True
      return False


    def deQueue(self):
      self.items.pop(0)

    def isEmpty(self):
      return self.items == []
    def size(self):
      return len(self.items)
    def getFront(self):
      return self.items[0][1]
    def __str__(self):
     if self.isEmpty():
      return 'Empty'
     else:
      return self.getFront()
       


inp1,inp2 = input('Enter Input : ').split('/')
inp1 = inp1.split(',')
inp2 = inp2.split(',')
employee = {}
# /////////// สร้าง dictionary เก็บ id ////////////
for e in inp1:
  a,b = e.split()
  department,id = int(a),int(b)
  employee[id] = department
# /////////// Command ////////////     
q = Queue()
for e in inp2:
  if e[0] == 'D':
    if not q.isEmpty():
      print(q.getFront())
      q.deQueue()
    else:
      print('Empty')
  else:
    a,b = e.split()
    id = int(b)
    q.insertQueue([employee[id],id])




  


