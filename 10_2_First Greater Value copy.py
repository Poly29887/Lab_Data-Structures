
def first_greater_value(arr, target):
    if len(arr) == 0:
        return None
    
    arr.sort()

    if arr[0] > target:
        return arr[0]
    if arr[-1] < target:
        return 'No First Greater Value'

    low = 0
    high = len(arr) - 1 

    while low <= high:
        mid = low + (high - low)//2

        if arr[mid] <= target:
            low = mid + 1
        else:
            ans = arr[mid]
            high = mid - 1
    
    return ans


arr, targets = input('Enter Input : ').split('/')
arr = list(map(int, arr.split(' ')))
targets = list(map(int, targets.split(' ')))

for target in targets:
    print(first_greater_value(arr, target))

# =============================== 2 =============================
def fm(lx,i):
    for j in lx:
        if i<j:
            return str(j)
    return "No First Greater Value"
x,y = input('Enter Input : ').split('/')
lx = [int(i) for i in x.split()]
ly = [int(i) for i in y.split()]
lx = sorted(lx)
for i in ly:
    print(fm(lx,i))

# ============================= 3 ===============================
def first_greater_value(lst, key):
    lst = sorted(lst)
    for item in lst:
        if item > key:
            return item
    return "No First Greater Value"


if __name__ == '__main__':
    inp = input("Enter Input : ").split('/')
    lst, key_lst = list(map(int, inp[0].split())), list(map(int, inp[1].split()))
    for key in key_lst:
        print(first_greater_value(lst.copy(), key))

# ============================= 4 ===============================
  
if __name__ == "__main__":
    inp = input('Enter Input : ').split('/')
    arr, arr2 = sorted(list(map(int, inp[0].split()))), list(
        map(int, inp[1].split()))
    #print(arr)
    for x in arr2:
        try:
            print(min(y for y in arr if y > x))
        except:
            print("No First Greater Value")


# ============================= 5 ===============================
def greaterThan(index, array, x):
    if index > len(array) - 1:              # base case
        return 'No First Greater Value'

    if array[index] <= x:
        return greaterThan(index + 1, array, x)     # recursive go to next index and return value back
    elif array[index] > x:                  # FOUND!!!
        return array[index]                         # return value greater than


inputlst, xlst = input('Enter Input : ').split('/')
inputlst = [int(i) for i in inputlst.split()]
xlst = [int(i) for i in xlst.split()]

inputlst.sort()     # must sorted becuz ez to find with this algorithm

for i in xlst:
    print(greaterThan(0, inputlst, i))  # insert left lst and right lst

"""
ให้น้องเขียนโปรแกรมหาค่าที่น้อยที่สุดที่มากกว่าค่าที่ต้องการจะหา ถ้าหากไม่มีให้แสดงว่า No First Greater Value โดยตัวเลขของทั้ง 2 list รับประกันว่าไม่เกิน 1000000

***** อธิบาย Test Case 2:
Left : [3, 2, 7, 6, 8]         Right : [5, 6, 12]
1. หาค่าที่น้อยที่สุดที่มากกว่า 5 จาก list (Left) จะได้เป็น 6
2. หาค่าที่น้อยที่สุดที่มากกว่า 6 จาก list (Left) จะได้เป็น 7
3. หาค่าที่น้อยที่สุดที่มากกว่า 12 จาก list (Left) จะเห็นว่าไม่มีค่าที่มากกว่า 12 จะแสดงเป็น No First Greater Value

Enter Input : 3 2 7 6 8/5 6 12
6
7
No First Greater Value
"""