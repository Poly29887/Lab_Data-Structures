class ManageStack():

    def __init__(self):
        self.list = []

    def add(self, i):
        self.list.append(int(i))
        print(f'Add = {i}')

    def pop(self):
        if len(self.list) == 0:
            print("-1")
        else:
            print(f'Pop = {self.list[-1]}')
            self.list.pop()

    def delete(self, i):
        self.deL = []
        if len(self.list) == 0:
            print("-1")
        else:
            while int(i) in self.list:
                self.list.remove(int(i))
                print(f'Delete = {i}')

    def lessThen(self, i):
        self.deL = []
        if len(self.list) == 0:
            print("-1")
        else:
            for j in range(0, len(self.list)):
                if self.list[j] < int(i):
                    self.deL.append(self.list[j])
            self.deL.reverse()
            for k in range(0, len(self.deL)):
                self.list.remove(self.deL[k])
                print(f'Delete = {self.deL[k]} Because {self.deL[k]} is less than {i}')

    def moreThen(self, i):
        self.deL = []
        if len(self.list) == 0:
            print("-1")
        else:
            for j in range(0, len(self.list)):
                if self.list[j] > int(i):
                    self.deL.append(self.list[j])
                    print(f'Delete = {self.list[j]} Because {self.list[j]} is more than {i}')
            for k in range(0, len(self.deL)):
                self.list.remove(self.deL[k])

    def __str__(self):
        return f'Value in Stack = {self.list}'


ip = [e for e in input("Enter Input : ").split(",")]

s = ManageStack()

for i in range(0,len(ip)):
    if ip[i] == 'P':
        s.pop()
    else:
        command, value = ip[i].split()
        if command == 'A':
            s.add(value)
        elif command == 'D':
            s.delete(value)
        elif command == 'LD':
            s.lessThen(value)
        else: s.moreThen(value)

print(s)