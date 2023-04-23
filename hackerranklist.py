'''l=[]
n=int(input())
for i in range(n):
    k=input().split(' ')
    
    if k[0]=='insert':
        l.insert(int(k[1]),int(k[2]))
    elif k[0]=='append':
        l.append(int(k[1]))
    elif k[0]=='pop':
        l.pop()
    elif k[0]=='remove':
        l.remove(int(k[1]))
    elif k[0]=='print':
        print(l)
    elif k[0]=='sort':
        l.sort()
    else:
        l.reverse()'''
n=int(input())
k=map(int,input().split())
t=tuple(k)
print(hash(t))
