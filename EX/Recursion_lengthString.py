count = 0
def length(txt):
    global count
    if txt != '':
        print(f'{txt[0]}*',end='')
        count += 1
        txt = txt[1:]
        if txt != '':
            print(f'{txt[0]}~',end='')
            count += 1
            length(txt[1:])

txt = str(input("Enter Input : "))
length(txt)
print()
print(count)