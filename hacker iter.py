l=list(map(int,input().split(' ')))
summ=0
for i in range(l[0]):
    k=list(set(map(int,input().split(' '))))
    summ+=max(k)**2
print(summ%l[1])
