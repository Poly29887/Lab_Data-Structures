print(" *** Divisible number ***")
inp = int(input("Enter a positive number : "))

num=0
if inp>0:
    print("Output ==> ",end="")
    for i in range(1,inp+1):
        if inp % i==0:
            print(i,end=" ")
            num+=1
    print("\nTotal ==>",num)
else:
    print(inp,"is OUT of range !!!")