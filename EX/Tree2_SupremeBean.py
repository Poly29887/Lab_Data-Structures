class Node:
    def __init__(self,key = None):
        self.rChild = None
        self.lChild = None
        self.parent = None
        self.data = key 
        self.turn = ''

class Tree:
    def __init__(self):
        self.root = None
        self.turn = ''
        self.size = 0

    def _printtree(self):
        self.printtree(self.root)
    
    def insert(self,someNumber):
        self.size = self.size+1
        if self.root is None:
            self.root = Node(someNumber)
            print('*')
        else:
            self.insertWithNode(self.root, someNumber)    
         
    def insertWithNode(self,node,someNumber):
        if node.lChild is None and node.rChild is None:
            if someNumber > node.data:
                newNode = Node(someNumber)
                node.rChild = newNode
                newNode.parent = node
                newNode.turn = node.turn + 'R'
                print(newNode.turn+'*')
            else:
                newNode = Node(someNumber)
                node.lChild = newNode
                newNode.parent = node
                newNode.turn = node.turn + 'L'
                print(newNode.turn+'*')
        else: 
            if someNumber > node.data:
                if node.rChild is not None:
                    self.insertWithNode(node.rChild, someNumber)
                else: 
                    newNode = Node(someNumber)
                    node.rChild = newNode
                    newNode.parent = node 
                    newNode.turn = node.turn + 'R'
                    print(newNode.turn+'*')
            else:
                if node.lChild is not None:
                    self.insertWithNode(node.lChild, someNumber)
                else:
                    newNode = Node(someNumber)
                    node.lChild = newNode
                    newNode.parent = node      
                    newNode.turn = node.turn + 'L'  
                    print(newNode.turn+'*')
        
t = Tree()
#input('Enter Input : ')
l = [int(e) for e in input('Enter Input : ').split()]
for i in l:
    t.insert(i)