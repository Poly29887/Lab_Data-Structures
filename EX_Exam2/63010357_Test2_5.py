class Queue():
    def __init__(self):
        self.Q=[]
        self.size=0

    def enQ(self,data):
        self.Q.append(data)
        self.size+=1
    
    def deQ(self):
        return self.Q.pop(0)
        self.size-=1

    def Size(self):
        return self.size

Q = Queue()
L,R = input("Enter Input : ").split("/")
L=list(L.split())
R=list(R.split(","))
for i in range(len(L)):
    Q.enQ(L[i])
for i in range(len(R)):
    order = R[i].split()
    if order[0] == "D":
        if Q.Size() != 0:
           Q.deQ()
    elif order[0] == "E":
        Q.enQ(order[1])
if len(Q.Q) != len(list(dict.fromkeys(Q.Q))):
    print("Duplicate")
else:
    print("NO Duplicate")