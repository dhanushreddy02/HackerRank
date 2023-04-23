'''import textwrap

def wrap(string, max_width):
    return list(textwrap.fill(string,max_width))
    

s=input()
j=int(input())
l=[]
l.append(wrap(s,j))
print(l)'''
from collections import OrderedDict
def removeDupWithOrder(str):
    return "".join(OrderedDict.fromkeys(str))
 
l=input()
j=0
k=len(l)
y=[]
i=0
x=int(input())
a=x
while j<k:
    y.append(l[i:x])
    i+=a
    x+=a
    j+=a

for i in y:
    print(removeDupWithOrder(i))
