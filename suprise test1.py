def fun_expanding(E):
    flag=True
    l=[]
    for i in range (len(E)):
        E[i]=int(E[i])
        a=abs(E[i]-E[i-1])
        l.append(a)
    for j in range (len(l)) :
        if l[i-1]>=l[i]:
            flag=False
            break
    return flag
E=[]
L=int(input("Enter length of list"))
for k in range(L):
    El=int(input("Enter element"))
    E.append(El)
print(fun_expanding(E))
