def iSort(lst,newl = [],n=1):
    if len(lst)>0:
        # print(newl,lst)
        compInsert(newl,lst.pop(0),len(newl)-1)
        if len(newl)>1:
            print(newl,end=" ")
            if len(lst)>0:
                print(lst)
            else:
                print('\n',"sorted\n",newl,sep="")
        iSort(lst,newl,n+1)
        
            
def compInsert(lst,a,ln):
    if len(lst)==0:
        lst.append(a)
        return
    if ln>=-1: 
        if ln ==-1:
            lst.insert(0,a)
            print("insert ",a," at index ",ln+1," : ",sep = "",end ="")
        elif a < lst[ln]:
            compInsert(lst,a,ln-1)
        else:
            lst.insert(ln+1,a)
            print("insert ",a," at index ",ln+1," : ",sep = "",end ="")

inp = [int(e) for e in input("Enter Input : ").split()]
iSort(inp)

"""
Enter Input : 1 2 8 6 3 4 -9
insert 2 at index 1 : [1, 2] [8, 6, 3, 4, -9]
insert 8 at index 2 : [1, 2, 8] [6, 3, 4, -9]
insert 6 at index 2 : [1, 2, 6, 8] [3, 4, -9]
insert 3 at index 2 : [1, 2, 3, 6, 8] [4, -9]
insert 4 at index 3 : [1, 2, 3, 4, 6, 8] [-9]
insert -9 at index 0 : [-9, 1, 2, 3, 4, 6, 8]
sorted
[-9, 1, 2, 3, 4, 6, 8]


Enter Input : 1 2 3 7 8
insert 2 at index 1 : [1, 2] [3, 7, 8]
insert 3 at index 2 : [1, 2, 3] [7, 8]
insert 7 at index 3 : [1, 2, 3, 7] [8]
insert 8 at index 4 : [1, 2, 3, 7, 8]
sorted
[1, 2, 3, 7, 8]
"""