l=list(map(int,input().split(' ')))
sum=0
X=[]
for i in range(l[1]):
    k=list(map(float,input().split(' ')))
    X.append(k)
print(zip(*X))
