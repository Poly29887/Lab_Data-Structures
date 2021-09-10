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
    def front(self):
       return self.items[0]
    def __str__(self):
      output = ''
      if not self.isEmpty():
        for e in self.items:
          output += e
      return output
class Stack:
    def __init__(self,list = None):
       if list == None:
        self.items = []
       else:
        self.items = list
    def push(self,i) :
       self.items.append(i)
    def pop(self):
       self.items.pop()
    def isEmpty(self):
       return self.items == []
    def size(self):
       return len(self.items)
    def top(self):
       return self.items[-1]  
    def front(self):
       return self.items[0] 
    def reverseOutput(self):
      r_output = ''
      if not self.isEmpty():
        tail = len(self.items)-1
        for i in range(tail,-1,-1):
          r_output += str(self.items[i])
      else:
        r_output = 'ytpmE'
      return r_output
    def __str__(self):
      output = ''
      if not self.isEmpty():
        for e in self.items:
          output += str(e)
      else:
        output = 'Empty'
      return output
  
normal,mirror=[],[]
normal[0:],mirror[0:]= input('Enter Input (Normal, Mirror) : ').split() #list[0:] = string -> เก็บstringเป็นlist
item = Queue()
s_mirror = Stack()
s_normal = Stack()
n_exNormal = 0 # Normal Explosive of Normal
n_exFail = 0 # Failed Interrupted of Normal
m_ex = 0 # Explosive of Mirror
count = 0

# manage mirror
mirror.reverse() 
last = mirror[len(mirror)-1]
for elem in mirror:
  if s_mirror.isEmpty():
    s_mirror.push(elem)
    count = 1
  else:
    if elem == last and s_mirror.size() == 2 and elem == s_mirror.top() and elem == s_mirror.front() :
      count = 3
    elif elem == s_mirror.top():
      count += 1
    else :
      count = 1
    
    if count == 3:
      s_mirror.pop()
      s_mirror.pop()
      item.enQueue(elem)
      count = 0
      m_ex += 1
    else: 
      s_mirror.push(elem) 

# manage normal 
last = normal[len(normal)-1]
for elem in normal:
  if s_normal.isEmpty():
    s_normal.push(elem)
    count = 1
  else:
    if elem == last and s_normal.size() == 2 and elem == s_normal.top() and elem == s_normal.front() :
      count = 3
    elif elem == s_normal.top():
      count += 1
    else :
      count = 1
    if count == 3 : 
      if not item.isEmpty(): 
       if elem == item.front():
        s_normal.pop()
        n_exFail += 1
        count = 1
       else:
        s_normal.push(item.front())
        s_normal.push(elem)
        count = 1
       item.deQueue()
      else:
        s_normal.pop()
        s_normal.pop()
        count = 0
        n_exNormal += 1
    else:
      s_normal.push(elem)
print('NORMAL :')
print(s_normal.size())
if s_normal.isEmpty():
  print('Empty')
else:
  print(s_normal.reverseOutput())
print(f'{n_exNormal} Explosive(s) ! ! ! (NORMAL)')
if n_exFail > 0:
  print(f'Failed Interrupted {n_exFail} Bomb(s)')
print('------------MIRROR------------') 
print(': RORRIM') 
print(s_mirror.size())
print(s_mirror.reverseOutput())
print(f'(RORRIM) ! ! ! (s)evisolpxE {m_ex}')



      
    






       
