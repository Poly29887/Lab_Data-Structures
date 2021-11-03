inp = int(input('Enter a positive number : '))
if inp < 0 :
  print(f'{inp} is too low.')
elif inp >= 16:
  print(f'{inp} is too high.')   
else:
  l_hex = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
  col1 = 2
  col_last = 1
  row1 = ''
  row_last = ''
  for i in range(1,inp+1):
     row1 += l_hex[i]+' '
  print(row1)
  for i in range(1,inp-1): #from (inp+1)-2
     print(l_hex[col1] + ' '*(((inp-2)*2)+1) + l_hex[col_last])
     col1 += 1
     col_last += 1
  row_last += l_hex[col1] + ' '
  for i in range(1,inp):
     row_last += l_hex[i]+' '
  print(row_last)
