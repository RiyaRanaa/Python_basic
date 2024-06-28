l=[4,5,3,2,1]
for i in range(0,len(l)):
    min1=i
    for j in range(i+1,len(l)):
        if l[j]<l[min1]:
            min1=j
    l[i],l[min1]=l[min1],l[i]
print(l)

