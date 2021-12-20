def power(list,n):
    p = 0
    if n >= len(list): 
        return 
    p += list[n]
    if (2*n)+1 < len(list) :
        p += list[(2*n)+1] 
    else :
        p += 0

    if (2*n)+2 < len(list) :
        p += list[(2*n)+2] 
    else :
        p += 0

    return p

inp = input('Enter Input : ').split('/')
data = [int(i) for i in inp[0].split()]
opr = inp[1].split(',')
sum = 0
for i in data:
    sum += i
print(sum)
for c in opr:
    n = [int(i) for i in c.split()]
    s1,s2 = str(n[0]),str(n[1])
    if power(data,n[0]) > power(data,n[1]):
        print(s1+'>'+s2)
    elif power(data,n[0]) < power(data,n[1]):
        print(s1+'<'+s2)
    else:
         print(s1+'='+s2)