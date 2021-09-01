def num_grid(lst):

 num_list = [[0] * 5 for i in range(5)]
 for i in range(0,len(lst)):
    c=0
    for j in lst[i]:
       if j == '-':
         num_list[i][c]=0
       else:
         num_list[i][c]='#'
       c+=1
 n = len(num_list[0])
 for row in range(n):
    col=0
    for x in num_list[row]:
        if x == '#':
            if col != 0 and num_list[row][col-1]!='#':
             num_list[row][col-1]+=1

            if col != n-1 and num_list[row][col+1]!= '#':
             num_list[row][col+1]+=1

            if row != 0 and num_list[row-1][col]!= '#':
             num_list[row-1][col]+=1

            if row != n-1 and num_list[row+1][col]!= '#':
             num_list[row+1][col]+=1

            if row != 0 and col != 0 and num_list[row-1][col-1]!= '#':
              num_list[row-1][col-1]+=1

            if row != 0 and col != n-1 and num_list[row-1][col+1]!= '#':
              num_list[row-1][col+1]+=1 

            if row != n-1 and col != 0 and num_list[row+1][col-1]!= '#':
              num_list[row+1][col-1]+=1

            if row != n-1 and col != n-1 and num_list[row+1][col+1]!= '#':
              num_list[row+1][col+1]+=1 

        col+=1

 for i in range(len(num_list[0])):
    j=0
    for x in num_list[0]:
       num_list[i][j]=str(num_list[i][j]) 
       j+=1

 return num_list



print('*** Minesweeper ***')
print('Enter input(5x5) : ')
lst_input = []

input_list = input().split(",")

for e in input_list:

  lst_input.append([i for i in e.split()])

print("",*lst_input,sep = "\n")

print("\n",*num_grid(lst_input),sep = "\n")



