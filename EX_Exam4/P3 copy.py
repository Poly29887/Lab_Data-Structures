comparison = 0
def swap(ls, x, last, lastNum):
    global comparison
    if x < 0:
        return ls, last
    else:
        ls, position = swap(ls, x-1, last, lastNum)

        if ls[last] < ls[x]:
            if ls[last] == lastNum:
                position = x
            temp = ls[last]
            ls[last] = ls[x]
            ls[x] = temp
            if x != 0:
                comparison += 1
        return ls, position

def insert(ls, n):
    if n == 0:
        return ls
    else:
        global comparison
        ls = insert(ls, n-1)
        last = n
        lastNum = ls[last]
        comparison += 1
        ls, position = swap(ls, n, last, lastNum)

    return ls

print(' *** Insertion sort ***')
inp = [int(i) for i in input('Enter some numbers : ').split()]
k = len(inp)-1
ls = insert(inp,k)
print()
print(ls)
print('Data comparison = ', comparison)