compare = 0
def mergeSort(l):
    global compare
    if len(l)>1:
        mid = len(l)//2
        left = l[:mid]
        right = l[mid:]
        mergeSort(left)
        mergeSort(right)
        c1, c2, c3 = 0, 0, 0
        while c1 < len(left) and c2 < len(right):
            if left[c1] < right[c2]:
                l[c3] = left[c1]
                c1 += 1
            else:
                l[c3] = right[c2]
                c2 += 1
            c3 += 1
            compare += 1
        while c1 < len(left):
            l[c3] = left[c1]
            c1 += 1
            c3 += 1
        while c2 < len(right):
            l[c3] = right[c2]
            c2 += 1
            c3 += 1       

print(' *** Merge sort ***')
inp = [int(i) for i in input('Enter some numbers : ').split(' ')]
mergeSort(inp)
print("\nSorted -> ", end='')
for i in range(len(inp)):
        print(inp[i], end=" ")
print('\nData comparison = ', compare)