def oddd(t):
    k=1
    for i in range(t):
        print(k)
        k+=2
def evenn(t):
    k=0
    for i in range(t):
        print(k)
        k+=2





n=int(input())
for i in range(n):
    li=list(input().split(' '))
    if li[0]=='odd':
        oddd(int(li[1]))
    else:
        evenn(int(li[1]))
   
