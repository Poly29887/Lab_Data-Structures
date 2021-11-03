def findGCD(a,b):
    if(b == 0):
        return a
    else:
        return findGCD(b,a%b)

inp =input('Enter Input : ').split()
inp = [int(i) for i in inp]
inp.sort()
if inp[0]<0 and inp[1]<0:
    inp.sort(reverse=True)
if abs(sum(inp))>0:
    print("The gcd of",inp[1],"and",inp[0],"is :",abs(findGCD(inp[1],inp[0])))
else:
    print("Error! must be not all zero.")