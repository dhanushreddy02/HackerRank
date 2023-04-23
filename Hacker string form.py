def ste(n):
    j=len(bin(n).replace('0b',''))
    
    for i in range(1,n+1):
        a=str(i).rjust(j)
        b=bin(i).replace('0b','').upper().rjust(j)
        c=hex(i).replace('0x','').rjust(j)
        d=oct(i).replace('0o','').rjust(j)
    return(a,d,c,b)
n=int(input())
print(ste(n))
    
