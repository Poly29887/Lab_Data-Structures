n_max = 0
def findmax(i,inp):
    global n_max
    if i == 0:
        n_max = int(inp[0])
    elif i == len(inp):
        return n_max
    else:
        if int(inp[i]) > n_max:
            n_max = int(inp[i])
    i+=1
    return findmax(i,inp)        

inp = input('Enter Input : ').split()
print('Max :',findmax(0,inp))