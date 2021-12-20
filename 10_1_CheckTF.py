def bi_search(l, r, arr, x):
    if l > r:
        return False

    mid = l + (r-l)//2
    if arr[mid] == x:
        return True
    elif arr[mid] > x:
        return bi_search(l, mid-1, arr, x)
    else:
        return bi_search(mid+1, r, arr, x)

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

# =================================== 2 ================================
def bi_search(index, lastIndex, array, x):
    if index > lastIndex:   # base case
        return False

    mid = (index+lastIndex)//2      # find middle of array

    if x == array[mid]:             # check middle itself
        return True
    elif x < array[mid]:                             # if x is less than middle
        return bi_search(index, mid-1, array, x)        # recursive left side
    elif x > array[mid]:                             # if x is more than middle
        return bi_search(mid+1, lastIndex, array, x)    # recursive right side

inp = input('Enter Input : ').split('/')
arr, k = list(map(int, inp[0].split())), int(inp[1])
print(bi_search(0, len(arr) - 1, sorted(arr), k))

"""
ให้น้องๆเขียน Binary Search โดยใช้ Recursive เพื่อหาว่ามีค่านั้นอยู่ใน list หรือไม่ ถ้าหากมีให้ตอบ True หากไม่มีให้ตอบ False

***** อธิบาย Input
1. ด้านซ้าย  จะเป็น list ของ Data
2. ด้านขวา   จะเป็นค่าที่เราต้องการจะหา

Enter Input : 33 2 11 82 77 28 15 76 9 64/28
True

Enter Input : 33 2 11 82 77 28 15 76 9 64/50
False


"""