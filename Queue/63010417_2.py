class Queue:
    def __init__(self,list = None):
      if list == None:
       self.items = []
      else:
        self.items = list
      self.special = [] #ตน.ที่มีกองกำลังสำรวจ
      self.num_sp = 0 #จน.กองกำลังสำรวจในแถว
    def enQueue(self,i,special = None):
      if special == 1:
        if 0 in self.special: #มีกองกำลังสำรวจที่หัวแถว(ตน.0)
         self.items.insert(1,i)
        else:
         self.items.insert(0,i)
        self.special.append(self.num_sp) #แทรกตน.ที่มีกองกำลังสำรวจ
        self.num_sp+=1 
      else:
        self.items.append(i)
    def deQueue(self):
      self.items.pop(0)
      if 0 in self.special: 
        i = 0
        self.special.pop() #เลื่อนไปตน.กองกำลังสำรวจ 
        self.num_sp-=1 
      
    def isEmpty(self):
      return self.items == []
    def size(self):
      return len(self.items)
    def getValue(self,i):
      return self.items[i]


inp = input('Enter Input : ').split(',')
q = Queue()


for e in inp:
  if len(e)>1:
   cm,value = e.split()
  else:
   cm = e
  if cm == 'EN':
   q.enQueue(value)
  elif cm == 'ES':
   q.enQueue(value,1) # special enqueue
  elif cm == 'D':
   if q.isEmpty():
     print('Empty')
   else:
     print(q.getValue(0))
     q.deQueue()
   

