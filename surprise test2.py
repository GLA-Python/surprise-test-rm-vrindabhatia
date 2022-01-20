def expanding_function(lst):
    l=[]
    flag=True
    for i in range (1,len(lst)):
        a=abs(lst[i]-lst[i-1])
        l.append(a)
    for j in range (1,len(l)):
        if l[j]<=l[j-1]:
            flag=False
            break
    return flag
lst=[]
N=int(input('enter length of list'))
for i in range (N):
    El=int(input("Enter element"))
    lst.append(El)
print(expanding_function(lst))
    
        
        
        
