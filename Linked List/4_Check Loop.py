class Node:
    def __init__(self, value,next = None):
        self.data = value
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
        self.isLoop = False

    def __str__(self): 
        if not self.isEmpty():
          s = ''
          now = self.head
          while now != None:
            s += str(now.data)          
            if now.next != None:
                s += '->'
            now = now.next
          return s
        else: 
          return 'Empty'

    def append(self, item):
        p = Node(item) 
        if self.head == None:
          self.head = p
          self.size = 1
        else :
          now = self.head 
          self.size = 1
          while now.next != None:
              now = now.next
              self.size +=1
          now.next = p
          self.size += 1 

    def showSize(self):
        return self.size

    def indexOf(self,data): # for search index of data
        now = self.head
        for i in range(self.showSize()):
           if now.data == data:
               return i
           now = now.next
        return -1
    def isIn(self,data):
        return self.indexOf(data) >= 0

    def nodeAt(self,i):
        now = self.head
        for j in range(0,i):
           now = now.next
        return now
    
    def isEmpty(self) :
        return self.size == 0

    def setNext(self,i1,i2):
        if self.isEmpty():
            print('Error! {list is empty}')
        elif i1 < 0 or i1 > self.showSize()-1:
            print('Error! {index not in length}: '+ str(i1))
        elif i2 < 0 or i2 > self.showSize()-1:
            self.append(i2)
            print(f'index not in length, append : {i2}')
        else: 
            n1 = self.nodeAt(i1)
            n2 = self.nodeAt(i2)
            n1.next = n2    
            print(f'Set node.next complete!, index:value = {i1}:{n1.data} -> {i2}:{n2.data}')
            if i1 >= i2:
               self.isLoop = True
    
    def checkLoop(self):
        if self.isLoop:
            print('Found Loop')
        else:
            print('No Loop')
            print(self)



l = SinglyLinkedList()
inp = input('Enter input : ').split(',')
for e in inp:
  cm,n = e.split(' ')
  if cm == 'A':
      l.append(n)
      print(l)
  else:
      i1,i2 = n.split(':')
      l.setNext(int(i1),int(i2))
l.checkLoop()

