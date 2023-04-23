from itertools import permutations
k=input().split(' ')
l=set()
c=''
n=1
while n<=int(k[1]):
    for i in (list(permutations(k[0],n))):
        for j in range(n):
            c=c+i[j]
        l.update(c)
        c=''
    n+=1
    print(l)
    

for i in l:
    print(i)
