count = 0
def shellSort(arr):
    n = len(arr)
    h = 8 // 2
    global count
    while h > 0:
        for i in range(h, n):
            temp = arr[i]
            j = i
            count += 1
            while j >= h and arr[j - h] > temp:
                count += 1
                arr[j] = arr[j - h]
                j -= h
            arr[j] = temp
        h //= 2
    return count


print(" *** Shell sort ***")
arr = [int(x) for x in input("Enter some numbers : ").split(" ")]
round = shellSort(arr)

print()
print(arr)
print("Data comparison =  {}".format(round))