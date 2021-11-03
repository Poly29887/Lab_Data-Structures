text_in = "Infix : "
text_pre = "Prefix : "

class Node:
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

class BST:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = Node(data)
        else:
            root = self.root
            while True:
                if data < root.data:
                    if root.left is None:
                        root.left = Node(data)
                        break
                    root = root.left
                else:
                    if root.right is None:
                        root.right = Node(data)
                        break
                    root = root.right
        return self.root
    def printTree(self, node, level=0):
        if node is not None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
def infix(T):
    global text_in
    if T is not None:
        if T.left is not None or T.right is not None:  
            text_in += "("
        infix(T.left)
        text_in += str(T.data)
        infix(T.right)
        if T.left is not None or T.right is not None: 
            text_in += ")"
            
def prefix(T):
    global text_pre
    if T is not None:
        text_pre += str(T.data)
        prefix(T.left)
        prefix(T.right)

inp = input("Enter Postfix : ")
T = BST()
s = Stack()
for ch in inp:
    if ch in '+-*/':
        op1 = s.pop()
        op2 = s.pop()
        s.push(Node(ch, op2, op1))
    else:
        s.push(Node(ch))
print("Tree :")
T.root = s.pop()
T.printTree(T.root)
print("--------------------------------------------------")
infix(T.root)
print(text_in)
prefix(T.root)
print(text_pre)