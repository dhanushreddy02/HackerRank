a=list(map(int,(input().split(' '))))
b=list(map(int,(input().split(' '))))
c=set(a)
d=set(b)
k=c.symmetric_difference(d)
l=list(k)
l.sort()
for i in l:
    print(i)
