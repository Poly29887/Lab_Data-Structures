def Left(s):
    H=s[-1]
    H+=s[:-1]
    return H

def Right(s):
    s=s[1:]+s[0]
    return s

print("*** String Rotation ***")
inp = input("Enter 2 strings : ").split()
L=inp[0]
R=inp[1]
i=1
while True:
    L=Left(L)
    R=Right(R)
    if L == inp[0] and R == inp[1]:
        if i > 5 and i !=6:
            print(" . . . . .")
        print(i, L, R)
        break
    if i <= 5:
        print(i, L, R)
    i+=1
    if L == inp[0] and R == inp[1]:
        break
print("Total of ",i,"rounds.")
