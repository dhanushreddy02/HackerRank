from itertools import combinations
n=list(input().split(' '))
k=list()
for i in range(1,int(n[1])+1):
    k.append(list(combinations(n[0],i)))
print(k)


