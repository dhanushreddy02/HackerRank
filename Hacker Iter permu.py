from itertools import permutations
k=input().split(' ')
l=[]
c=''
for i in (list(permutations(k[0],int(k[1])))):
    for j in range(int(k[1])):
        c=c+i[j]
    l.append(c)
    c=''
l.sort()
for i in l:
    print(i)
