class Stack:
    def __init__(self,list = None):
       self.count=0
       if list == None:
        self.items = []
       else:
        self.items = list
    def push(self,i) :
       self.items.append(int(i))
       print('Add = {}'.format(i))
    def pop(self):
       print('Pop = {}'.format(self.peek()))
       self.items.pop()
    def peek(self):
       return self.items[-1]       
    def isEmpty(self):
       return self.items == []
    def size(self):
       return len(self.items)
    def delete(self,i):
       temp = []
       for e in self.items:
          if e != i:
            temp.append(e)
          else:
           print('Delete = {}'.format(i))
       self.items = temp

    def less_del(self,i):
       temp = []
       for e in self.items:
          if e < i:
            print('Delete = {} Because {} is less than {}'.format(e,e,i))
          else :
            temp.append(e)
       self.items = temp
    def more_del(self,i):
       temp = []
       for e in self.items:
          if e > i:
            print('Delete = {} Because {} is more than {}'.format(e,e,i))
          else :
            temp.append(e)
       self.items = temp       

temp = [e for e in input('Enter Input : ').split(',')]
inp=[]
for e in temp:
    inp.append(e.split())
i=0
s=Stack()
while i < len(inp):
    if  inp[i][0]== 'A':
        s.push(int(inp[i][1]))
    elif s.isEmpty() == True :
        print('-1')
    elif  inp[i][0]== 'P':
        s.pop()
    elif inp[i][0] == 'D':
        s.delete(int(inp[i][1]))
    elif  inp[i][0]== 'LD':
        s.less_del(int(inp[i][1]))
    elif inp[i][0] == 'MD':
        s.more_del(int(inp[i][1]))
    i+=1
print('Value in Stack =', s.items)



