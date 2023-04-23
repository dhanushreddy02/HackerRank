n=int(input())
l=list(map(int,input().split(' ')))
d={}
op=0
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
j=int(input())
for i in range(j):
    z=list(map(int,input().split(' ')))
    if z[0] in d and d[z[0]]!=0:
        op+=z[1]
        d[z[0]]-=1
print(op)
    
