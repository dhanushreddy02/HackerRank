l=list(map(int,input().split(' ')))
ma=0
for i in range(l[0]):
    k=set(map(int,input().split(' ')))
    ma+=max(k)**2

print(ma%l[1])
