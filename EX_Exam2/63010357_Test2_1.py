class Stack:
    def __init__(self):
        self.item=[]
        self.Size=0
    
    def __str__(self):
        s = "Data in Stack is : "+" ".join(list(map(str,self.item)))
        return s

    def push(self,data):
        self.item.append(data)
        self.Size +=1

    def pop(self):
        self.Size -=1
        return self.item.pop()

    def isEmpty(self):
        return self.Size==0

    def size(self):
        return self.Size

    def peek(self):
        return self.item[-1]

    def bottom(self):
        return self.item[0]

inp = input("Enter choice : ")
if inp == "1":
    s1 = Stack()
    s1.push(10)
    s1.push(20)
    print(s1)
    s1.pop()
    s1.push(30)
    print("Peek of stack :",s1.peek())
    print("Bottom of stack :",s1.bottom())
elif inp == "2":
    s1 = Stack()
    s1.push(100)
    s1.push(200)
    s1.push(300)
    s1.pop()
    print(s1)
    print("Stack is Empty :",s1.isEmpty())
elif inp == "3":
    s1 = Stack()
    s1.push(11)
    s1.push(22)
    s1.push(33)
    s1.pop()
    print(s1)
    print("Stack size :",s1.size())