class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self):
        return str(self.data)

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None :
          self.root = Node(data)
          print('*')
        else:
          now = self.root
          while True :
            if data < now.data :
                if now.left is None : 
                    now.left = Node(data)
                    print('L',end='')
                    print('*')
                    break
                print('L',end='')
                now = now.left
            else : 
                if now.right is None : 
                    now.right = Node(data)
                    print('R',end='')
                    print('*')
                    break
                print('R',end='')
                now = now.right
        return self.root
           
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)

