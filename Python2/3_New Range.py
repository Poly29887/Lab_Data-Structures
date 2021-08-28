def range(list_num):
    if(len(list_num)==1):
      i=0
      temp=[]
      while i < list_num[0]:
          temp.append(float(i))
          i+=1
    if(len(list_num)==2):  
      i=list_num[0]
      temp=[]
      while i < list_num[1]:
          temp.append(float(i))
          i+=1  
      
    if(len(list_num)==3):  
      i=list_num[0]
      step = list_num[2]
      temp=[]
      while i < list_num[1]:
          temp.append(float(i))
          i=i+step
      
    
    numtuple = tuple(temp)
    return numtuple


print('*** New Range ***')
list = [float(e) for e in input("Enter Input : ").split()]
print(range(list))

