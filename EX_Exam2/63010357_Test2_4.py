class LinkedList:
    class Node :
        def __init__(self,data,next = None) :
            self.data = data
            if next is None :
                self.next = None
            else :
                self.next = next
                
        def __str__(self) :
            return str(self.data)

    def __init__(self,head = None):
        if head == None:
                self.DummyHead = self.Node(None)
                self.Tail = self.DummyHead
                self.size = 0
            
    def __str__(self) :
        s = ''
        p = self.DummyHead.next
        for i in range(self.size):
            if i < self.size-1:
                s += str(p.data)+' <- '
            elif i == self.size-1:
                s += str(p.data)
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.DummyHead == None:
            self.DummyHead.next = self.Tail = p
        else:
            t = self.Tail
            t.next = p   
            self.Tail =p  
        self.size += 1

    def removeHead(self) :
        if self.head == None : return
        if self.head.next == None :
            p = self.head
            self.head = None
        else :
            p = self.head
            self.head = self.head.next
        self.size -= 1
        return p.data

    def isEmpty(self) :
        return self.size == 0
    
    def nodeAt(self,i) :
        p = self.DummyHead.next
        for j in range(i) :
            p = p.next
        return p

    def indexOf(self,data):
        current = self.DummyHead.next
        for i in range(self.size):
            if current.data == data:
                return i
            current = current.next
        return-1
    
    def sort(self):
        if self.DummyHead.next != self.nodeAt(self.indexOf("0")):
            p= self.nodeAt(self.indexOf("0")-1)
            head = p.next
            p.next = None
            current = head
            while current.next != None:
                current = current.next
            current.next= self.DummyHead.next
            self.DummyHead.next=head
print(" *** Re order ***")
inp = input("Enter Input : ").split()
ll = LinkedList()
for i in range(len(inp)):
    ll.append(inp[i])
print("Before :",ll)
ll.sort()
print("After :",ll)
