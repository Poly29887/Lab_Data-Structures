def binary(now,n,digits):
    if now == n:
        s = bin(now) #bin(int) decimal->binary 
        print(s[2:].zfill(digits)) #zfill(len) เติม 0 หน้า string จนครบจน.len
        return n
    else:
        s = bin(now)
        print(s[2:].zfill(digits))
        return binary(now+1,n,digits)

    

inp = int(input('Enter Number : '))
if inp < 0:
    print('Only Positive & Zero Number ! ! !')
else:
    num = 2**inp-1
    binary(0,num,inp)