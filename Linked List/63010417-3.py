class Node :
    def __init__(self,data,prev = None,next = None) :
        self.data = data
        if prev is None :
            self.prev = None
        else :
            self.prev = prev
        if next is None :
            self.next = None
        else :
            self.next = next

class DoublyLinkedList :    
    def __init__(self):                
            self.head = None
            self.size = 0
            
    def __str__(self): 
        s = ''
        if not self.isEmpty():
          now = self.head
          while now != None:
            s += str(now.data)          
            if now.next != None:
                s += ' '
            now = now.next
        return s

    def revStr(self): 
        rs = ''
        if not self.isEmpty():
          now = self.head
          while now.next != None: # find last node
            now = now.next
          while now != None:
            rs += str(now.data)    
            if now.prev != None:
                rs += ' '
            now = now.prev
        return rs

    def __len__(self) :
        return self.size   

    def isEmpty(self) :
        return self.size == 0

    def append(self,data) :
        p = Node(data)
        if self.isEmpty():
           self.head = p
        else:
         now = self.head
         while now.next != None:
             now = now.next
         p.prev = now
         now.next = p
        self.size += 1 

    def appendNode(self,newNode) :
        p = newNode
        if self.isEmpty():
           self.head = p
        else:
         now = self.head
         while now.next != None:
             now = now.next
         p.prev = now
         now.next = p
        self.size += 1 

    def addHead(self,data):
        p = Node(data)
        if self.head == None:
           self.head = p
        else :
           self.head.prev = p
           p.next = self.head
           self.head = p 
        self.size += 1
        return p    
    
    def showSize(self):
        if self.size == 0:
            return 0 
        else:
            return self.size

    def insert(self,index,data):
        if index < 0 or index > self.showSize(): 
           return 'Data cannot be added'
        elif index == 0 :
           self.addHead(data)
           return f'index = {index} and data = {data}'
        elif index == self.size or self.isEmpty():
           self.append(data)
           return f'index = {index} and data = {data}'
        else:
            q = self.nodeAt(index)
            p = Node(data,q.prev,q)
            q.prev.next = p
            q.prev = p 
            self.size += 1
            return f'index = {index} and data = {data}'
            
    def remove(self,data):
        i_node = self.indexOf(data)
        if i_node < 0 or self.isEmpty():      
           return 'Not Found!' 
        else:
           p = self.nodeAt(i_node)
           if self.size == 1:
             self.head = None
           elif i_node == 0:
             self.head = p.next
             p.next.prev = None
           elif i_node == self.size-1: 
             p.prev.next = None
           else:
             q = p.next
             p.prev.next = p.next
             p.next.prev = p.prev
           self.size -= 1
           return f'removed : {p.data} from index : {i_node}'

    def nodeAt(self,i) :
        p = self.head
        for j in range(0,i) :
            p = p.next   
        return p

    def indexOf(self,data) :
        q = self.head
        for i in range(self.size) :
            if q.data == data :
                return i
            q = q.next
        return -1    

    def listOfData(self):
        ld = []
        if not self.isEmpty():
          now = self.head
          while now != None:
            ld.append(now.data)  
            now = now.next
        return ld
       
    


f_inp = input('Enter Input (L1,L2) : ').split()
inp1 = f_inp[0].split('->')
inp2 = f_inp[1].split('->')
l_1 = DoublyLinkedList()
l_2 = DoublyLinkedList()
for e in inp1:
   l_1.append(e)
for e in inp2:
   l_2.append(e)
print(f'L1    : {l_1}')
print(f'L2    : {l_2}')
rl_2 = l_2.listOfData()
rl_2.reverse()
for e in rl_2:
    l_1.append(e)
print(f'Merge : {l_1}')
