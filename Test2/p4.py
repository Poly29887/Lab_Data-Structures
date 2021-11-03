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
                self.head = self.tail = None
                self.size = 0
        else:
            self.head = head
            t = self.head        
            self.size = 1
            while t.next != None :
                t = t.next
                self.size += 1
            self.tail = t
            
    def __str__(self) :
        s = 'Linked data : '
        p = self.head
        while p != None :
            s += str(p.data)+' '
            p = p.next
        return s

    def __len__(self) :
        return self.size
    
    def append(self, data):
        p = self.Node(data)
        if self.head == None:
            self.head = self.tail = p
        else:
            t = self.tail
            t.next = p   
            self.tail =p  
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
        p = self.head
        for j in range(i) :
            p = p.next
        return p
    
    def removeDup(self) :
        temp = []
        p = self.head 
        while p.next != None:
            temp.append(p.data)
            if p.next.data in temp:
              if p.next.next == None:
               p.next = None
              else :
               p.next = p.next.next
              self.size -= 1
            else:
              p = p.next
        
    def contentEquivalence(self,list2):
        self.removeDup()
        if self.size != len(list2):
            return False
        l2_data = []
        q = list2.head
        while q != None:
            l2_data.append(q.data)
            q = q.next
        p = self.head
        while p.next != None :
            ch = 0 
            for e in l2_data:
              if p.data == e:
                  ch += 1
            if ch !=1 : return False
            p = p.next
        return True

        
inp1,inp2 = input('List1,List2 : ').split(', ')
inp1 = inp1.split()
inp2 = inp2.split()
l1 = LinkedList()
l2 = LinkedList()
for e in inp1:
    l1.append(e)
for e in inp2:
    l2.append(e)
print(f'List1 content Equivalence List2 : {l1.contentEquivalence(l2)}')   

