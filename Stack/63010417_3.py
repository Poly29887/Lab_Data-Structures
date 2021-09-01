class Stack:
    def __init__(self,list = None):
       if list == None:
        self.items = []
       else:
        self.items = list
    def push(self,i) :
       self.items.append(i)
    def pop(self):
       self.items.pop()
    def isEmpty(self):
       return self.items == []
    def size(self):
       return len(self.items)

