from collections import defaultdict
d=defaultdict(list)
l=[]
x=''
n=list(map(int,input().split(' ')))
for i in range(1,n[0]+1):
    d[input()].append(i)
for i in range(n[1]):
    l.append(input())
for i in d:
    if i in l:
        x=''.join(str(d[i]))
        print(x)
