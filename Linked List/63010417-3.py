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
