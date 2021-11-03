print(" *** String count ***")
inp = input("Enter message : ").split()
s=""
numUp=0
numLow=0
listUp=[]
listLow=[]
for i in range(len(inp)):
    s+=inp[i]
for i in s:
    if ord(i) >= ord("A") and ord(i) <= ord("Z"):
        numUp+=1
        if i not in listUp:
            listUp.append(i)
    elif ord(i) >= ord("a") and ord(i) <= ord("z"):
        numLow+=1
        if i not in listLow:
            listLow.append(i)

listUp=sorted(listUp)
listLow=sorted(listLow)
print("No. of Upper case characters :",numUp)
print("Unique Upper case characters :","  ".join(listUp))
print("No. of Lower case Characters :",numLow)
print("Unique Lower case characters :","  ".join(listLow))

