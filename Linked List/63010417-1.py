class Node:
    def __init__(self, value,next = None):
        self.data = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0
    def __str__(self):
        if self.isEmpty():
            return "Empty"
        now, s = self.head, str(self.head.data) + " "
        while now.next != None:
            s += str(now.next.data) + " "
            now = now.next
        return s

    def isEmpty(self):
        return self.head == None

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
        
    def addHead(self, item):
        p = Node(item)
        if self.size > 0:
            p.next = self.head
        self.head = p
        self.size += 1

    def search(self, item):
         if self.index(item) >= 0 : 
             return 'Found'
         else :
             return 'Not Found'

    def index(self, data):
         now = self.head
         for i in range(self.size):
            if now.data == data:
             return i
            now = now.next 
         return -1

    def sizeShow(self):
        return str(self.size)

    def pop(self, pos):
        if pos > self.size-1 or pos < 0:
         return 'Out of Range'
        else:
         if pos == 0:
          self.head = self.head.next
          self.size -= 1
         else: 
          p = self.head
          if self.size > 0:
           for j in range(0,pos-1) : # หาตำแหน่ง node
            p = p.next
          p.next = p.next.next
          self.size -= 1
         return 'Success'


L = LinkedList()
inp = input('Enter Input : ').split(',')
for i in inp:
    if i[:2] == "AP":
        L.append(i[3:])
    elif i[:2] == "AH":
        L.addHead(i[3:])
    elif i[:2] == "SE":
        print("{0} {1} in {2}".format(L.search(i[3:]), i[3:],L))
    elif i[:2] == "SI":
        print("Linked List size = {0} : {1}".format(L.sizeShow(), L))
    elif i[:2] == "ID":
        print("Index ({0}) = {1} : {2}".format(i[3:], L.index(i[3:]), L))
    elif i[:2] == "PO":
        before = "{}".format(L)
        k = L.pop(int(i[3:]))
        print(("{0} | {1}-> {2}".format(k, before, L)) if k == "Success" else ("{0} | {1}".format(k, L)))
print("Linked List :", L)