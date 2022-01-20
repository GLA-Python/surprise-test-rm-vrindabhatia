def Look_and_Say(a):
    lst = []
    i = 0
    while i <len(a):
        j= 1
        while i+1<len(a) and a[i]==a[i+1]:
            i+= 1 
            j+= 1 
        lst.append(str(j)+a[i])
        i+= 1 
    return ''.join(lst)
   
row = int(input())
num= int(input())
for i in range (row):
    print(num)
    num= Look_and_Say(str(num))
