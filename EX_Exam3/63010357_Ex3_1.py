x = ""
def harmonic_sum(n):
    result = 0
    if n==1:
        global x
        x+= str(n)+" "
        return 1
    result += 1/n + harmonic_sum(n-1)
    x += str(1) + "/"+str(n)+" "
    return result

print(" *** Harmonic sum ***")
num = int(input("Enter number of terms : ")) 
y=harmonic_sum(num)
z=x.split()
print(" + ".join(z),"= ",end="")
print("%.8f" %(y))