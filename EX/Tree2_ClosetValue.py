class Node:
    def __init__(self,key = None):
        self.rChild = None
        self.lChild = None
        self.parent = None
        self.data = key 

class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def _printtree(self):
        self.printtree(self.root)
    def _search(self,key):
        return self.search(self.root,key) 
    def _maxValue(self):
        return self.maxValueNode(self.root).data
    def insert(self,someNumber):
        self.size = self.size+1
        if self.root is None:
            self.root = Node(someNumber)
        else:
            self.insertWithNode(self.root, someNumber)    
         
    def insertWithNode(self,node,someNumber):
        if node.lChild is None and node.rChild is None:
            if someNumber > node.data:
                newNode = Node(someNumber)
                node.rChild = newNode
            else:
                newNode = Node(someNumber)
                node.lChild = newNode  
        else: 
            if someNumber > node.data:
                if node.rChild is not None:
                    self.insertWithNode(node.rChild, someNumber)
                else: 
                    newNode = Node(someNumber)
                    node.rChild = newNode 
            else:
                if node.lChild is not None:
                    self.insertWithNode(node.lChild, someNumber)
                else:
                    newNode = Node(someNumber)
                    node.lChild = newNode
    def printtree(self, node, level = 0) :
        if node != None:
            self.printtree(node.rChild, level + 1)
            print('     ' * level, node.data)
            self.printtree(node.lChild, level + 1)
    def search(self,root,key):
        if root is None or root.data == key:
            return root is not None
        if root.data < key:
            return self.search(root.rChild,key)
        return self.search(root.lChild,key)
    def maxValueNode(self,current):
        while(current.rChild is not None):
            current = current.rChild
        return current
    def closestValue(self,value):
        root = self.root
        print('Closest value of',str(value),':',end=' ')
        for i in range(int(1e12)):
            if self._search(value+i):
                print(value+i)
                break
            elif self._search(value-i):
                print(value-i)
                break
    
t = Tree()
s = input('Enter Input : ').split('/')
l = [int(e) for e in s[0].split()]
k = int(s[1])
for i in l:
    t.insert(i)
    t._printtree()
    print('--------------------------------------------------')

t.closestValue(k)