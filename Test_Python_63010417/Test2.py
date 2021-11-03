inp = int(input('Input : '))
if inp > 0:
    print('')
    for i in range(1,inp+1):
        print('*' * i + ' ' * ((inp-i)*2) + '*' * i )
    for i in range(1,inp+1):
        print('*' * (inp-i) + ' ' * (i*2) + '*' * (inp-i) )
else:
    print('!!!Please enter number greater than zero!!!')