class Node:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def __str__(self):
        return str(self.data)
class BST:
    def __init__(self):
        self.root=None

    def insert(self,data):
        if self.root == None:
            self.root = Node(data)
        else:
            current = self.root
            while(1):
                if data<current.data:
                    if current.left != None:
                        current = current.left
                    else:
                        current.left = Node(data)
                        return self.root
                else:
                    if current.right != None:
                        current = current.right
                    else:
                        current.right = Node(data)
                        return self.root

    def preOrder(self,node=-1):
        if node ==-1:
            node = self.root
        if node != None:
            print(node.data,end=" ")
            self.preOrder(node.left)
            self.preOrder(node.right)

    def postOrder(self,node=-1):
        if node ==-1:
            node = self.root
        if node != None:
            self.postOrder(node.left)
            self.postOrder(node.right)
            print(node.data,end=" ")
        
    def inOrder(self,node=-1):
        if node ==-1:
            node = self.root
        if node != None:
            self.inOrder(node.left)
            print(node.data,end=" ")
            self.inOrder(node.right)
            
    def LevelOrder(self):
        x=list()
        x.append(self.root)
        while x:
            y=x.pop(0)
            print(y,end=" ")
            if y.left:
                x.append(y.left)
            if y.right:
                x.append(y.right)

T=BST()
print(" *** Binary Search Tree ***")
inp = [int(i) for i in input("Enter Input : ").split()]
for i in range(len(inp)):
    root = T.insert(inp[i])
print("")
print(" --- Tree traversal ---")
print("Level order : ",end="")
T.LevelOrder()
print("")
print("Preorder : ",end="")
T.preOrder()
print("")
print("Inorder : ",end="")
T.inOrder()
print("")
print("Postorder : ",end="")
T.postOrder()
