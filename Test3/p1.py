def natural_sum(n):
    if n == num :
        print(n,'= ',end='')
        return n
    else:
        print(n,'+ ',end='')
        return natural_sum(n+1) + n

    
global num
print(' *** Natural sum ***')
num = int(input("Enter number : ")) 
print("%.d" %(natural_sum(1)))