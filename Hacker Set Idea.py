a=input()
b=list(map(int,input().split(' ')))
c=set(map(int,input().split(' ')))
d=set(map(int,input().split(' ')))
k=0
for i in b:
    if i in c:
        k+=1
for i in b:
    if i in d:
        k-=1
print(k)
