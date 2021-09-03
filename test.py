def manangeStack(command,value = None):
  if value == None:
   print('no value')
  else:
   print(value)
  
manangeStack(2,3)
manangeStack(2)

list = [3,3,1,3,2]
sum = 0
for e in list:
  if int(e) == 3:
    list.remove(e)
print(list)