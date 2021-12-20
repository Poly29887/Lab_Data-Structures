
def fm(lx,i):
    for j in lx:
        if i<j:
            return str(j)
    return "No First Greater Value"
x,y = input('Enter Input : ').split('/')
lx = [int(i) for i in x.split()]
ly = [int(i) for i in y.split()]
lx = sorted(lx)
for i in ly:
    print(fm(lx,i))

