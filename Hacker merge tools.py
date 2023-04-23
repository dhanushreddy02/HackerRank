import textwrap
n='AABACAADA'
z=(len(n)//3)
j=list(textwrap.fill(n,z))
res = []
[res.append(x) for x in j if x not in res]
print(res)
 
