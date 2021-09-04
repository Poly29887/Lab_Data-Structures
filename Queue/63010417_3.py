class Queue:
    def __init__(self,list=None):
      if list == None:
       self.items = []
      else:
       self.items = list
    def enQueue(self,i):
      self.items.append(i)
    def deQueue(self):
      self.items.pop(0)
    def isEmpty(self):
      return self.items == []
    def size(self):
      return len(self.items)
    def getValue(self,i):
      return self.items[0]
    def __str__(self):
      return q.items

def secretCode(code,hint=None,step=None):
  output = ''
  num = 0
  if hint == None:
      output = chr(ord(code)+step) #chr() - Char -> ASCII
      return output
  else:
      num = ord(hint)-ord(code) #ord() - ASCII -> Char
      return num


code,hint = input('Enter code,hint : ').split(',')
q = Queue()
step = secretCode(code[0],hint)
for e in code:
  q.enQueue(secretCode(code=e,hint=None,step=step))
  print(q.items)