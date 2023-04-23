n=list(map(int,input().split(' ')))
x=[]

for i in range(n[1]):
    x.append(list(map(float,input().split(' '))))
print(zip(*x))
