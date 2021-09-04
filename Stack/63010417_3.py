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
    def top(self):
       return self.items[-1]

infix = input('Enter Infix : ')
s = Stack()
postfix = ''
operator=[')','(','^','*','/','+','-']
for e in infix:
   if e not in operator:
      postfix += e
   elif s.isEmpty():
      s.push(e)
   elif e == '(':
      s.push(e)
   elif e == ')':
      while s.top() != '(':
        postfix += s.top()
        s.pop()
      s.pop() #pop (
   elif e == '^':
        while s.top() == '^':
         postfix += s.top()
         s.pop()
         if s.isEmpty : break
        s.push(e)
   elif e in '*/':
        while s.top() in '^*/':
         postfix += s.top()
         s.pop()
         if s.isEmpty : break
        s.push(e)
   elif e in '+-':
      if not s.isEmpty():
        while s.top() in '^*/+-':
         postfix += s.top()
         s.pop()
         if s.isEmpty() : 
            break
        s.push(e)
while not s.isEmpty():
   postfix += s.top()
   s.pop()    
print(f'Postfix : {postfix}')

