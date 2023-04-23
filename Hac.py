from itertools import combinations
k=int(input())
c=0
z=[i for i in range(1,k+1)]
j=list(input().split())
m=int(input())
l=list(combinations(z,m))
print(l)
for i in l:
    for j in i:
        for k in range(1,m+1):
            if k==j:
                print(k)
                c+=1
print(c)
