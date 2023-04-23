def cap(s):
    k=''
    s=list(s.split(' '))
    for i in range(len(s)):
        if i==0:
            k=k+(str(s[i]).capitalize())
        else:
            k=k+' '+(str(s[i]).capitalize())
    return k
s=input()
print(cap(s))
