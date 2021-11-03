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

    def order(self,data):
        if self.head == None:
            self.append(data)
        else:
            t = self.tail
            if data >= t.data: #ใส่ที่หาง
              self.append(data)
            else:
              
        self.size += 1

    def append(self, data):  
        return self.insertAfter(self.size,data)
    
    def insertAfter(self, i, data):		
        p = self.nodeAt(i-1)
        p.next = self.Node(data, p.next)
        self.tail = p.next
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
    
    def findMean(self):
        pass


    def findMedian(self):
        pass
        
inputlist = [int(e) for e in input('Enter numbers : ').split()]

l = LinkedList()
for e in inputlist :
    l.append(e)
print("Output :")
print(l)
print('Amount of data =',len(l))
findMean(l)
findMedian(l)