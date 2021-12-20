
class Data:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return "({0}, {1})".format(self.key, self.value)

class hash:
    def __init__(self, table_size, max_collisions):
        self.table_size = table_size
        self.max_collisions = max_collisions
        self.store = [None for _ in range(self.table_size)]
        self.size = 0

    def is_full(self):
        if self.size == self.table_size:
            print("This table is full !!!!!!")
            return True
        return False

    def insert(self, key, value):
        if self.is_full():
            return

        hashed_value = 0
        for c in key:
            hashed_value += ord(c)
        hashed_value = hashed_value%self.table_size

        first_hashed_value = hashed_value

        collision_count = 0
        while self.store[hashed_value] is not None:
            collision_count += 1
            print(f"collision number {collision_count} at {hashed_value}")

            if collision_count >= self.max_collisions:
                print("Max of collisionChain")
                return

            n = collision_count
            hashed_value = (first_hashed_value + n * n)%self.table_size

        self.store[hashed_value] = Data(key, value)
        self.size += 1

    def print_table(self):
        for i, ele in enumerate(self.store):
            print(f"#{i+1}\t{ele}")





print(" ***** Fun with hashing *****")
arr, pair = input("Enter Input : ").split("/")
table_size, max_collisions = arr.split(" ")
pair = [ p.split(" ") for p in pair.split(",")]

hash_table = hash(int(table_size), int(max_collisions))
for p in pair:
    if hash_table.is_full():
        break
    hash_table.insert(p[0], p[1])
    hash_table.print_table()
    print("---------------------------")

# ============================ 2 =============================
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


"""
ให้น้องเขียน Hashing โดยมีการทำงานดังนี้

1. หา index ของ Table จากผลรวมของ ASCII จากค่า key จากนั้นนำมา mod ด้วยขนาดของ Table
2. หากเกิด Collision ให้ทำการขยับค่า index แบบ Quadratic Probing
3. ถ้าหากเกิด Collision จนถึงค่าที่กำหนดแล้ว ให้ทำการ Discard Data นั้นทิ้งทันที
4. หาก Table นั้นมี Data เต็มแล้วให้แสดงคำว่า This table is full !!!!!! หากเคยแสดงคำนี้ไปแล้วไม่ต้องแสดงอีก (แสดงเพียง 1 ครั้ง)

อธิบาย Input
แบ่ง Data เป็น 2 ชุดด้วย /
    -   ด้านซ้ายหมายถึง ขนาดของ Table และ MaxCollision ตามลำดับ
    -   ด้านขวาหมายถึง Data n ชุด โดย Data แต่ละชุดแบ่งด้วย comma โดยใน Data แต่ละชุดจะแบ่งเป็น key กับ value ตามลำดับ


     ***** Fun with hashing *****
Enter Input : 3 2/1+1 I,OnE Love,abcde I,#$ew2 KMITL,kk KMITL,z Love
#1	(1+1, I)
#2	None
#3	None
---------------------------
collision number 1 at 0
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
collision number 1 at 0
collision number 2 at 1
Max of collisionChain
#1	(1+1, I)
#2	(OnE, Love)
#3	None
---------------------------
#1	(1+1, I)
#2	(OnE, Love)
#3	(#$ew2, KMITL)
---------------------------
This table is full !!!!!!

"""