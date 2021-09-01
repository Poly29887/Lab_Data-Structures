num_list = [int(i) for i in input('Enter Your List : ').split()]
sum0 = []
answer = []

if len(num_list) <= 2:
    print('Array Input Length Must More Than 2')
else:
    for a in range(len(num_list)):
       for b in range(len(num_list)):
           for c in range(len(num_list)): 
                 if a<b<c:  
                   if num_list[a] + num_list[b] + num_list[c] == 0:
                       sum0.append(num_list[a])
                       sum0.append(num_list[b])
                       sum0.append(num_list[c])
                       sum0.sort()
                       if sum0 not in answer:
                           answer.append(sum0)
                       sum0 = []
    print(answer)




