lis=[]
for i in range(int(input())):
    name = input()
    marks=input(float())
    lis.append([name,marks])
sort=sorted(list(set([x[1] for x in lis])))
second=sort[1]
fin=[]
for k in lis:
    if k[1]==second:
        low.append(k[0])
for j in sorted(low):
    print(j)
   
