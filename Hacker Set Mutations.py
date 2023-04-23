su=0
n=int(input())
s=set(input().split(' '))
k=int(input())
for i in range(k):
    y=input().split(' ')
    j=set(input().split(' '))
    if y[0]=='intersection_update':
        s.intersection_update(j)
       
        
    if y[0]=='update':
        s.update(j)
       
        
        
    if y[0]=='symmetric_difference_update':
                 s.symmetric_difference_update(j)
                
    if y[0]== 'difference_update':
        s.difference_update(j)
       
        
                 
for i in s:
    su=su+int(i)
print(su)

                 
