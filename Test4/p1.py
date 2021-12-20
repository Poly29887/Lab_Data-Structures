class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None



def list_to_bst(l_num):
    if len(l_num)>1:
        mid = int(len(l_num)/2)
        node = TreeNode(l_num[mid])
        if mid != 0:
            temp = list_to_bst(l_num[:mid])
            node.left = temp
        if mid != len(l_num)-1:
            temp = list_to_bst(l_num[mid+1:])
            node.right = temp
        return node
    else:
        node = TreeNode(l_num[0]) 
        return node    

       

def preOrder(node): 
    if not node: 
        return      
    print(node.val)
    preOrder(node.left) 
    preOrder(node.right)  


def printBST(node,level = 0):
    if node != None:
        printBST(node.right, level + 1)
        print('     ' * level, node.val)
        printBST(node.left, level + 1)


l_num = sorted([int(item) for item in input("Enter list : ").split()])
result = list_to_bst(l_num)

print("\nList to a height balanced BST : ")
print(preOrder(result))
print("\nBST model : ")
printBST(result)

