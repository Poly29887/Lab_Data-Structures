def put_to_box(start_idx, weight):
    cur_idx = start_idx
    while weight - arr[cur_idx] >= 0:
        weight -= arr[cur_idx]
        cur_idx += 1
        if cur_idx >= len(arr):
            break

    return cur_idx

def is_valid(weight):
    cur_idx = 0

    for _ in range(box_num):
        cur_idx = put_to_box(cur_idx, weight)
        if cur_idx >= len(arr):
            return True

    if cur_idx >= len(arr):
        return False

arr, box_num = input("Enter Input : ").split("/")
arr = list(map(int, arr.split(" ")))
box_num = int(box_num)

w = max(max(arr), sum(arr)//box_num)
while True:
    if is_valid(w):
        break
    w += 1

print(f"Minimum weigth for {box_num} box(es) = {w}")

# ================================ 2 ==============================
def mw(lis, box): 
    if box == 1:
        return sum(lis)
    minw = sum(lis)+1
    for i in range(len(lis)):
        if len(lis[i:]) < box - 1:
            break
        tb = sum(lis[:i])
        ob = mw(lis[i:], box - 1)
        minw = min(max(tb, ob),minw)
    return minw
x, y = input("Enter Input : ").split('/')
lst = [int(i) for i in x.split()]
print(f'Minimum weigth for {y} box(es) = {mw(lst, int(y))}')

# ================================== 3 ==============================
def minimumWeight(lst, box):
    if box == 1:    # base case
        return sum(lst)

    minWeight = 99999  # init new min weight (infinity+++)
    for index in range(len(lst)):   # loop all index // find all possible way to push in the box...

        if len(lst[index:]) < box-1:    # if len of goods less than all box
            break

        leftValue = sum(lst[:index])    # [,i) # sum of my box (left side)
        rightValue = minimumWeight(lst[index:], box - 1)  # [i,) # recursive go to next box (right side)

        minWeight = min(max(leftValue, rightValue), minWeight)  # find lowest of sum of every set of box

    return minWeight


weightlst, k = input('Enter Input : ').split('/')
k = int(k)
weightlst = [int(i) for i in weightlst.split()]

ans = minimumWeight(weightlst, k)
print(f'Minimum weigth for {k} box(es) = {ans}')


"""
มีสินค้าอยู่ n ชิ้น โดยชิ้นที่ i (0 <= i < n) มีน้ำหนัก Wi กิโลกรัม  นำสินค้าบรรจุใส่กล่องไม่เกิน k ใบ โดยมีเงื่อนไขว่า
1. สิ่งของต้องมีน้ำหนักรวมกันไม่เกินน้ำหนักมากสุดที่กล่องรับไหว
2. หากสิ่งของชิ้นที่ a และชิ้นที่ b อยู่ในกล่องเดียวกัน (a <= b) สิ่งของทุกชิ้นที่อยู่ระหว่างสองชิ้นนี้ (ทุกชิ้นที่ i ที่ a < i < b) จะต้องอยู่ในกล่องนี้ด้วย (นั่นคือสิ่งที่ของในกล่องเดียวกันจะต้องเป็นสิ่งของที่ตำแหน่งติดกัน)

ถ้าทุกกล่องสามารถรับน้ำหนักได้เท่ากัน จงหาว่าเราสามารถใช้กล่องที่รับน้ำหนักได้น้อยสุดเท่าใด โดยที่ยังบรรจุของตามเงื่อนไขได้ และใช้กล่องครบทุกใบ

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง สินค้า n ชิ้น และแต่ละชิ้นมีน้ำหนัก W กิโลกรัม
    -   ด้านขวาหมายถึง จำนวนกล่อง k ใบ

คำใบ้  Optimization Problem


อธิบาย Test Case #1

มีสินค้าอยู่ 5 ชิ้น โดยมีน้ำหนักเป็น 6 2 4 3 7 ตามลำดับ และมีกล่องจำนวน 3 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 8 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 6 และ 2   กล่องใบที่ 2 จะใส่สินค้า 2 ชิ้นที่มำน้ำหนัก 4 และ 3  และกล่องใบที่ 3 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 7

อธิบาย Test Case #2

มีสินค้าอยู่ 10 ชิ้น โดยมีน้ำหนักเป็น 8 7 2 5 1 10 9 2 3 5 ตามลำดับ และมีกล่องจำนวน 5 ใบ   และน้ำหนักที่น้อยที่สุดที่สามารถใส่สินค้าได้ครบทุกชิ้น และใส่ลงกล่องได้ทุกใบคือ 14 กิโลกรัม โดยในกล่องที่ 1 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 8   กล่องใบที่ 2 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 7 2 และ 5   กล่องใบที่ 3 จะใส่สินค้า 2 ชิ้นที่มีน้ำหนัก 1 และ 10   กล่องใบที่ 4 จะใส่สินค้า 3 ชิ้นที่มีน้ำหนัก 9 2 และ 3    และกล่องใบที่ 5 จะใส่สินค้า 1 ชิ้นที่มีน้ำหนัก 5

Enter Input : 19 1 2 3 4/1
Minimum weigth for 1 box(es) = 29
"""