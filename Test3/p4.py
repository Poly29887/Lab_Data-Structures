class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def __str__(self) :
        return str(self.data)
    

class BinarySearchTree:
    def __init__(self) :
        self.root = None
    def create(self,data):
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

def height( node, level=0):
    if node != None:
        l.append(level)
        height(node.right, level + 1)
        height(node.left, level + 1)
        return str(max(l))
    return str(max(l))

print(" *** Binary Search Tree Height ***")
global l
l = []
tree = BinarySearchTree()
arr = list(map(int, input("Enter Input : ").split()))
for e in arr:
   tree.create(e)
print("Height = ",height(tree.root),end="\n\n")


