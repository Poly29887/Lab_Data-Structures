inp = [int(i) for i in input('Enter Input : ').split()]
output = ''
for i in range(0,len(inp)-1):
    if inp[i] <= inp[i+1]:
        output = 'Yes'
    else:
        output = 'No'
print(output)