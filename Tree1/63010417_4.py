class Queue :
    def __init__(self):
        self.items = []

    def __str__(self):
        return ' '.join(self.items)

    def enqueue(self, data):
        self.items.append(data)

    def dequeue(self):
        if not self.isEmpty():
         return self.items.pop(0)

    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0


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

    def pre_order(self, node):
        if node == None:
            return ''
        s =  str(node.data) + ' ' + self.pre_order(node.left) + self.pre_order(node.right)
        return s
        
        
    def in_order(self, node):
        if node == None:
            return ''
        s =  self.in_order(node.left) + str(node.data) + ' ' + self.in_order(node.right)
        return s
        

    def post_order(self, node):
        if node == None:
            return ''
        s =  self.post_order(node.left) + self.post_order(node.right) + str(node.data) + ' ' 
        return s
    
    def breath(self,node):
        q = Queue()
        output = ''
        q.enqueue(node)
        while not q.isEmpty():
            node_now = q.dequeue()
            output += str(node_now.data) + ' '
            if node_now.left is not None:
               q.enqueue(node_now.left)
            if node_now.right is not None:
               q.enqueue(node_now.right)
        return output
        
    
    def printTree(self, node, level = 0):
        if node != None:
            self.printTree(node.right, level + 1)
            print('     ' * level, node)
            self.printTree(node.left, level + 1)
        
T = BST()
inp = [int(i) for i in input('Enter Input : ').split()]
for i in inp:
    root = T.insert(i)
print('Preorder :',T.pre_order(root))
print('Inorder :',T.in_order(root))
print('Postorder :',T.post_order(root))
print('Breadth :',T.breath(root))