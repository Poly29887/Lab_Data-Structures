def findMax(m,l):
    if l==[]:
        return m
    if m == None:
        m=l[0]
    elif l[0]>m:
        m=l[0]
    return findMax(m,l[1:])

inp = input("Enter Input : ").split()
inp = [int(i) for i in inp]
print("Max :",findMax(None,inp))