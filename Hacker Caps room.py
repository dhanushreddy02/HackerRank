n=int(input())
l=input().split(' ')
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]+=1
print(min(d,key=d.get))
