
class Hash:
    def __init__(self, table_size, max_collisions, threshold):
        self.table_size = table_size
        self.max_collisions = max_collisions
        self.threshold = threshold
        self.store = [None for _ in range(self.table_size)]
        self.sequence = []
        self.size = 0

    def check_over_threshold(self, val):
        if (self.size/self.table_size) * 100 > self.threshold:
            print("****** Data over threshold - Rehash !!! ******")
            self.rehash(val)
            return True
        return False

    def insert(self, value):
        self.size += 1
        if self.check_over_threshold(value):
            return

        hashed_value = value%self.table_size

        first_hashed_value = hashed_value

        collision_count = 0
        while self.store[hashed_value] is not None:
            collision_count += 1
            print(f"collision number {collision_count} at {hashed_value}")

            if collision_count >= self.max_collisions:
                print("****** Max collision - Rehash !!! ******")
                self.rehash(value)
                return

            n = collision_count
            hashed_value = (first_hashed_value + n * n)%self.table_size

        self.store[hashed_value] = value
        self.sequence.append(value)

    def is_prime(self, x):
        return all(x % i for i in range(2, x))

    def next_prime(self, x):
        return min([a for a in range(x+1, 2*x) if self.is_prime(a)])

    def rehash(self, val):
        self.table_size = self.next_prime(self.table_size*2)
        self.size = 0

        self.store = [None for _ in range(self.table_size)]


        arr = self.sequence.copy()
        self.sequence.clear()
        for ele in arr:
            if ele is not None:
                self.insert(ele)

        self.insert(val)


    def print_table(self):
        for i, ele in enumerate(self.store):
            print(f"#{i+1}\t{ele}")


print(" ***** Rehashing *****")
arr, arr2 = input("Enter Input : ").split("/")
table_size, max_collisions , threshold = list(map(int, arr.split(" ")))
arr = arr2.split(" ")

h = Hash(table_size, max_collisions, threshold)
print("Initial Table :")
h.print_table()
print("----------------------------------------")
for ele in arr:
    print(f"Add : {ele}")
    h.insert(int(ele))
    h.print_table()
    print("----------------------------------------")


"""
ให้น้องๆเขียนการทำ Rehashing ด้วยเงื่อนไขดังนี้
1. Table เต็มถึงระดับที่กำหนด ( Threshold (%) )
2. เมื่อเกิดการ Collision ถึงจำนวนที่กำหนด

หากเกิดการ Rehashing ให้ทำการขยาย Table เป็นค่า prime ถัดไปที่มากกว่าเดิม 2 เท่า เช่น หาก Table ตอนแรกมีขนาด 4 และเกิดการ Rehashing  ตัว Table ใหม่จะมีขนาดเป็น 11 เนื่องจาก 2 เท่าของ 4 คือ 8  และค่า prime ที่มากกว่า 8 และใกล้ 8 มากที่สุดคือ 11

การ Hash หากเกิดการ Collision ให้ใช้ Quadratic Probing ในการแก้ปัญหา Collision

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table , MaxCollision และ Threshold (สูงสุด 100 %) ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย spacebar และ Data แต่ละตัวเป็นจำนวนเต็มศูนย์หรือบวกเท่านั้น และไม่มี Data ซ้ำกันเด็ดขาด

 ***** Rehashing *****
Enter Input : 5 1 67/1 6
Initial Table :
#1	None
#2	None
#3	None
#4	None
#5	None
----------------------------------------
Add : 1
#1	None
#2	1
#3	None
#4	None
#5	None
----------------------------------------
Add : 6
collision number 1 at 1
****** Max collision - Rehash !!! ******
#1	None
#2	1
#3	None
#4	None
#5	None
#6	None
#7	6
#8	None
#9	None
#10	None
#11	None
----------------------------------------
"""

############################### 2 ################################
class hash:

    def __init__(self,tablesize,maxcolision,threshold,datalst = []):
        self.tablesize = tablesize
        self.table = ["None" for i in range(self.tablesize)]
        self.maxcolision = maxcolision
        self.threshold = threshold
        self.datalst = datalst
        self.item = 0
    def __str__(self):
        sout = ""
        for i in range(len(self.table)):
            sout+="#"+str(i+1)+"	"+str(self.table[i])+"\n"
        return sout+"----------------------------------------"
    def rehashing(self):
        newsize = nextprime(self.tablesize*2)
        self.table = ["None" for i in range(newsize)]
        self.tablesize = newsize
        for i in range(self.item):
            self.hiddenprobe(self.datalst[i])       
        
        
    def qprobe(self,data,f=0):
        if (self.item+1)/self.tablesize > self.threshold/100:
            print("****** Data over threshold - Rehash !!! ******")
            while((self.item+1)/self.tablesize > self.threshold/100):
                self.rehashing()

            self.qprobe(data)
        else:
            index = (data+f**2)%self.tablesize
            if self.table[index] == "None":
                self.table[index] = data
                self.item+=1
                print(self)
            else:
                print("collision number {0} at {1}".format(f+1,index))
                if f+1>=self.maxcolision:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehashing()
                    self.qprobe(data)
                else:
                    self.qprobe(data,f+1)
    def hiddenprobe(self,data,f = 0):
        if (self.item+1)/self.tablesize > self.threshold/100:
            # print("****** Data over threshold - Rehash !!! ******")
            self.rehashing()
            self.hiddenprobe(data)
        else:
            index = (data+f**2)%self.tablesize
            if self.table[index] == "None":
                self.table[index] = data
                # print(self)
            else:
                print("collision number {0} at {1}".format(f+1,index))
                if f+1>=self.maxcolision:
                    print("****** Max collision - Rehash !!! ******")
                    self.rehashing()
                    self.hiddenprobe(data)
                else:
                    self.hiddenprobe(data,f+1)
def isprime(n,a=2):
    if n<=1:
        return
    else:
        if a>=n:
            return True
        elif n==2:
            return True
        elif n%a == 0:
            return False
        else:
            return isprime(n,a+1)
def nextprime(n):
    if not isprime(n+1):
        return nextprime(n+1)
    else:
        return n+1
        
print(" ***** Rehashing *****")
inp = input("Enter Input : ").split("/")

h = hash(int(inp[0].split()[0]),int(inp[0].split()[1]),int(inp[0].split()[2]),[int(i) for i in inp[1].split()])
print("Initial Table :\n",h,sep = "")
for i in inp[1].split():
    print("Add :",int(i))
    h.qprobe(int(i))

    # ============================ 3 ==============================

class Data:
    def __init__(self, key, value):     # like a dict() with homemade class
        self.key = key
        self.value = value

    def __str__(self):
        return f'({self.key}, {self.value})'


class hash:
    def __init__(self, size, maxCol):
        self.lst = [None] * size        # lst of None (table size)
        self.maxCol = maxCol            # maxCollision
        self.tableSize = size           # table size
        self.realSize = 0               # init size (0)

    def printTable(self):
        for i in range(self.tableSize):         # print table size
            print(f'#{i+1}\t{self.lst[i]}')
        print('---------------------------')

    def insert(self, key, value):
        if self.realSize == self.tableSize:
            return False                    # table is full / cannot insert

        newData = Data(key, value)          # assign newData
        sum = 0
        for i in key:
            sum += ord(i)
        indexFirst = sum % self.tableSize   # find first index

        for n in range(self.maxCol):
            index = (indexFirst + n**2) % self.tableSize        # quadratic Probing +0 +1 +4 +9 ... n^2

            if self.lst[index] is not None:
                print(f'collision number {n+1} at {index}')     # collision with something...
            else:
                self.lst[index] = newData           # assign newData to table[index]
                self.realSize += 1                  # realSize++
                break                               # break out if already assign...
        else:
            print('Max of collisionChain')          # Max Collision

        return True     # can insert

# 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love

print(' ***** Fun with hashing *****')
inp = input('Enter Input : ').split('/')
tableSize, maxColis = map(int, inp[0].split())
lst = inp[1].split(',')

hashTable = hash(tableSize, maxColis)

for i in lst:
    i = i.split()
    canInsert = hashTable.insert(i[0], i[1])    # Insert .. and get can/cannot Insert

    if canInsert is True:                   # can insert .. print table
        hashTable.printTable()
    else:
        print('This table is full !!!!!!')  # cannot insert .. don't print table .. and break out!
        break