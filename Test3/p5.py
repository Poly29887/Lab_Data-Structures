class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) :
        return str(self.data)


class BST:
    def __init__(self) :
        self.root = None
    def insert(self,data):
        if self.root is None :
          self.root = Node(data)
        else:
          now = self.root
          while True :
            if data < now.data :
                if now.left is None : 
                    now.left = Node(data)
                    break
                now = now.left
            else : 
                if now.right is None : 
                    now.right = Node(data)
                    break
                now = now.right
        return self.root

    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)

    def findMin(self,node):
        n_min = 0
        if node != None:
            now = node
            while now is not None:
                n_min = now.data
                now = now.left
            return n_min
            
    def findMax(self,node):
        n_max = 0
        if node != None:
            now = node
            while now is not None:
                n_max = now.data
                now = now.right
            return n_max


T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
T.printTree(root)
print('-' * 50)
print('Min :',T.findMin(root))
print('Max :',T.findMax(root))