class Queue:
    def __init__(self,lst = None):
        self.lst = lst if lst is not None else []
    def size(self):
        return len(self.lst)
    def isEmpty(self):
        return len(self.lst) == 0
    def top(self):
        return self.lst[0]
    def enqueue(self,obj):
        self.lst.append(obj)
    def dequeue(self):
        return self.lst.pop(0)
    def show(self):
        return self.lst

f = open('file/users.txt', 'r', encoding='utf8')
s = f.readlines()
loginDetail=Queue()
if s != None:
    for line in s:
        loginDetail.enqueue())

f.close()   