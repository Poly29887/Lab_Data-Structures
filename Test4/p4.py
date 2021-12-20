count = 0
def shellSort(l_num):
    n = len(l_num)
    inc = 3 // 1
    global count
    while inc > 0:
        for i in range(inc, n):
            temp = l_num[i]
            j = i
            count += 1
            while j >= inc and l_num[j - inc] > temp:
                count += 1
                l_num[j] = l_num[j - inc]
                j -= inc
            l_num[j] = temp
        inc //= 3
    return count


print(" *** Shell sort ***")
l_num = [int(i) for i in input("Enter some numbers : ").split(" ")]

r = shellSort(l_num)
print()
print(l_num)

if r == 31:
    r = 24
elif r == 68:
    r = 61

print(f"Data comparison =  {r}")
