from collections import defaultdict
l=input().split(' ')
k=defaultdict(list)
z=[]
for i in range(int(l[0])):
    k[input()].append(i+1)
for i in range(int(l[1])):
    z.append(input())
for i in z:
    if i in k:
        for x in k[i]:
            print(x,end=' ')
        print()
    else:
        print(-1)
    
    
