from itertools import combinations_with_replacement
k=input().split(' ')
x=[]
c=''
l=sorted(k[0])
for i in (list(combinations_with_replacement(l,int(k[1])))):
    for j in range(int(k[1])):
        c=c+i[j]
    x.append(c)
    print(c)
    c=''
