'''9
1 2 3 4 5 6 7 8 9
10
pop
remove 9
discard 9
discard 8
remove 7
pop 
discard 6
remove 5
pop 
discard 5'''
su=0
n=int(input())
s=set(map(int,input().split(' ')))
k=int(input())
for i in range(k):
    y=input().split(' ')
    if y[0]=='pop':
        s.pop()
        
    if y[0]=='remove':
        s.remove(int(y[1]))
        
    if y[0]=='discard':
                 s.discard(int(y[1]))
                 
for i in s:
    su=su+i
print(su)

                 
