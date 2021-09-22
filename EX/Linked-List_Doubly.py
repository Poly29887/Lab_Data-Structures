class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList():
    def __init__(self):
        self.head = None

    def pushHead(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        newNode.next = self.head
        self.head.prev = newNode
        self.head = newNode

    def pushTail(self,data):
        newNode = Node(data)
        if self.head is None:
            self.head = newNode
            return
        now = self.head
        while now.next != None:
            now = now.next
        now.next = newNode
        newNode.next = None
        newNode.prev = now

    def insert(self,index,data):
        if index < 0 or index > self.len():
            return 'Data cannot be added'
        if self.head == None and index == 0:
            self.pushTail(data)
            return 'index = ' + str(index) + ' and data = ' + data
        elif index == 0:
            self.pushHead(data)
            return 'index = ' + str(index) + ' and data = ' + data
        elif index == self.len():
            self.pushTail(data)
            return 'index = ' + str(index) + ' and data = ' + data
        ide = 0
        now = self.head
        newNode = Node(data)
        while ide != index:
            ide += 1
            now = now.next
        if now.prev != None:
            now.prev.next = newNode
            newNode.prev = now.prev
            now.prev = newNode
            newNode.next = now
        return 'index = ' + str(ide) + ' and data = ' + data

    def popHead(self):
        self.head = self.head.next
        self.head.next = None

    def popTail(self):
        newNode = self
        if self.head is None:
            self = newNode
            return
        now = self.head
        while now.next.next:
            now = now.next
        now.next = None
    
    def remove(self,data):
        if self.head is None:
            return 'Not Found!'
        delNode = Node(data)
        now = self.head
        ide = 0
        while now != None:
            if now.data == delNode.data:
                if now.prev != None:
                    now.prev.next = now.next
                elif now.prev is None and now.next is None:
                    self.head = None
                else:
                    now.next.prev = None
                    self.head = now.next
                if now.next != None:
                    now.next.prev = now.prev
                elif now.next is None and now.prev is not None:
                    now.prev.next = None
                break
            now = now.next
            ide += 1
        return 'removed : ' + delNode.data + ' from index : ' + str(ide)

    def len(self):
        now = self.head
        len = 0
        while now != None:
            len += 1
            now = now.next
        return len

    def isEmpty(self):
        return self.head == None

    def __str__(self):
        now = self.head
        s = ''
        while now != None:
            s += str(now.data)
            if now.next != None:
                s += '->'
            now = now.next
        return s
    
    def revStr(self):
        now = self.head
        s = ''
        temp = None
        while temp != now:
            temp = now
            if now.next != None:
                now = now.next     
        while now != None:
            s += str(now.data)
            if now.prev != None:
                s += '->'
            now = now.prev
        return s
                
    def isIn(self,data):
        now = self.head
        while now != None:
            if now == data:
                return True
            now = now.next
        return False

inp = input('Enter Input : ').split(',')
ll = LinkedList()
s = 0
for i in inp:
    temp = i.split()
    if temp[0] == 'A':
        ll.pushTail(temp[1])
    elif temp[0] == 'Ab':
        ll.pushHead(temp[1])
    elif temp[0] == 'I':
        a = temp[1].split(':')
        print(ll.insert(int(a[0]),a[1]))
    elif temp[0] == 'R':
        print(ll.remove(temp[1]))
    print('linked list :',ll)
    print('reverse :',ll.revStr())