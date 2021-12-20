comparison = 0
def swap(l_num, x, last, lastNum):
    global comparison
    if x < 0:
        return l_num, last
    else:
        ls, position = swap(l_num, x-1, last, lastNum)

        if l_num[last] < l_num[x]:
            if l_num[last] == lastNum:
                position = x
            temp = l_num[last]
            l_num[last] = l_num[x]
            l_num[x] = temp
            if x != 0:
                comparison += 1
        return ls, position

def insert(l_num, n):
    if n == 0:
        return l_num
    else:
        global comparison
        l_num = insert(l_num, n-1)
        last = n
        lastNum = l_num[last]
        comparison += 1
        l_num, position = swap(l_num, n, last, lastNum)
    return l_num

print(' *** Insertion sort ***')
inp = [int(i) for i in input('Enter some numbers : ').split()]
index = len(inp)-1
l = insert(inp,index)

print()
print(l)
print('Data comparison = ', comparison)