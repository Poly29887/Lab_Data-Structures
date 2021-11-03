
n_min = 0
def Min(index,l):
    global n_min 
    if index == 0:
       n_min = l[0]
    elif index == len(l):
        return n_min
    else:
        if inp[index] < n_min:
            n_min = l[index] 
    return Min(index+1,l)


inp = [int(i) for i in input('Enter Input : ').split()]
print(f'Min : {Min(0,inp)}',)
