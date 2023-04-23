n=input().split(' ')
'''for i in range(n):
    k=int(input())
    s=set(map(int,input().split(' ')))
    y=int(input())
    r=set(map(int,input().split(' ')))
    print(s.issubset(r))
    for i in range(1,int(n[1])+1):
    k=[]
    k=list(combinations(y,i))
    k.sort()
    for i in k:
        i=list(i)
        op=''
        for ele in i:
            op+=ele
        print(op)'''
y=list(n[0])

from itertools import combinations,permutations
k=list(combinations(y,2))

k.sort()
for i in k:
    print(i)



