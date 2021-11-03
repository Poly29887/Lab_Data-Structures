def isInList(l,num):
 check = False   
 for e in l:
     if e == str(num):
        check = True
 return check


l_inp = []
l_inp = input('Enter number end with (-1) : ').split()

l_f = []
l_num = []
if isInList(l_inp,-1):
  for n in l_inp:
      if n == '-1':
          break  
      if isInList(l_num,n):
          index = l_num.index(n)
          l_f[index] += 1
      else :
          l_num.append(n)
          l_f.append(1)
  if l_f == [] or max(l_f) == min(l_f):
      print('Not found')
  elif max(l_f) != min(l_f):
      print(l_num[l_f.index(max(l_f))])
else:
  print('Invalid INPUT !!!')


