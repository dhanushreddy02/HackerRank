from itertools import product
a=list(map(int,input().split(' ')))
b=list(map(int,input().split(' ')))
c=[]
c.append(a)
c.append(b)
for i in (list(product(*c))):
    print(i,end=' ')
