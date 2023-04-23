n=list(map(int,input().split(' ')))
a=set(map(int,input().split(' ')))
b=set(map(int,input().split(' ' )))
k=0
for i in a:
    if i in n:
        k+=1
print(k)
for i in b:
    if i not in n:
    
        k-=1
print(k)
